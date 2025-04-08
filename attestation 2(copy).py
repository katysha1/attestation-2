from abc import ABC, abstractmethod
import uuid
from _datetime import datetime
from typing import Dict, List, Optional, Any
import asyncio
import random
from uuid import uuid4


class Command(ABC):  # Абстрактный класс команды
    def __init__(self, description):
        self.id = str(uuid4())
        self.description = description
        self.time = datetime.now()

    def __str__(self):
        return f"Задача номер (ID={self.id}: '{self.description}', от {self.time})"

    @abstractmethod
    def execute(self):
        pass


class TaskManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.queue = []

        return cls._instance

    def add_task(self, task):
        self.queue.append(task)
        print(f'Задача {task.description} добавлена в очередь. Всего задач: {len(self.queue)}')

    def bubble_sort(self, id):  # пузырьковая сортировка by id

        n = len(id)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if id[j] > id[j + 1]:
                    id[j], id[j + 1] = id[j + 1], id[j]
                    swapped = True
            if not swapped:
                break
        return id
        print("\nСписок задач отсортированных по времени:")

    def linear_search(self, target):  # Линейный поиск id.
        print("Поиск задачи по id:")
        for task in self.queue:
            if task.id == target:
                print(f"Задача '{target}' найдена: {task}")
                return task
        print(f"Задача '{target}' не найдена.")
        return None

    def delete_task(self, id):
        # id_del = input("Введите id задачи для удаления")
        if not len(self.queue) == 0:
            return self.queue.pop()
        raise IndexError("Задачи отсутствуют")

    def print_task_list(self, task=None):
        if task:
            print(f"{task}")
        else:
            for i, task in enumerate(self.queue, 1):
                print(f"{i}. {task}")

    # def execute_all(self):
    #     pass

    async def execute_all(self):
        async def execute_task(task):
            await asyncio.sleep(5)
            task.execute()
            print(f"\nЗавершено:")

        tasks = [asyncio.create_task(execute_task(task)) for task in self.queue]
        await asyncio.gather(*tasks)

    def save_tasks(self, filename="tasks.txt"):
        with open(filename, "w") as f:
            for task in self.queue:
                f.write(f"{task.id},{task.description},{task.time}\n")
        print(f"Задачи сохранены в файл: {filename}")

    def load_tasks(self, filename="tasks.txt"):
        self.queue = []
        with open(filename, "r") as f:
            for line in f:
                id, description, time_str = line.strip().split(",")
                time = datetime.fromisoformat(time_str)
                task = PrintList(description)
                task.id = id
                task.time = time
                self.queue.append(task)
        print(f"Задачи загружены из файла: {filename}")


# Конкретные классы команд
class PrintList(Command):
    def __init__(self, id):
        super().__init__(id)
        self.id = id

    def execute(self):
        TaskManager().print_task_list(self)


class AddTask(Command):
    def __init__(self, *tasks):
        self.tasks = tasks

    def execute(self):
        for task in self.tasks:
            TaskManager().add_task()


class BubbleSort(Command):  # класс для пузырьковой сортировки
    def __init__(self, id):
        self.id = id

    def execute(self):
        TaskManager().bubble_sort()


class LinearSearch(Command):
    def __init__(self, id):
        self.id = id

    def execute(self):
        TaskManager().linear_search()


class DeleteTask(Command):
    def __init__(self, id):
        self.id = id

    def execute(self):
        TaskManager().delete_task()


# ПРИМЕНЕНИЕ
manager = TaskManager()
manager.load_tasks()
# print("\nСписок задач:")
# manager.print_task_list()

async def main():
    await manager.execute_all()


asyncio.run(main())

# Загрузка списка задач
# manager.add_task(PrintList("Скачивание файла"))
# manager.add_task(PrintList("Обработка данных"))
# manager.add_task(PrintList("Резервное копирование"))
# manager.add_task(PrintList("Синхронизация"))
# manager.add_task(PrintList("Анализ логов"))
# manager.add_task(PrintList("Экспорт данных"))
# manager.add_task(PrintList("Импорт данных"))
# manager.add_task(PrintList("Очистка кеша"))
# manager.add_task(PrintList("Обновление системы"))
# manager.add_task(PrintList("Мониторинг ресурсов"))
#
# manager.execute_all()
#
# # Печать списка задач
# print("\nСписок задач:")
# manager.print_task_list()
# manager.save_tasks()

# # Поиск задачи по ID
# manager.load_tasks()
# manager.linear_search("20fe5400-d922-4713-9504-3d1346efd996")

# # Печать списка задач
# manager.load_tasks()
# print("\nСписок задач:")
# manager.print_task_list()

# Удаление задачи по ID
# manager.load_tasks()
# manager.linear_search("cab5e0e2-66dc-4ffc-acbe-52df2c3249bc") #поиск задачи по id для удаления
# manager.delete_task("cab5e0e2-66dc-4ffc-acbe-52df2c3249bc") #удаление задачи по найденному id
# print("Задача удалена")
# print("\nСписок задач:")
# manager.print_task_list()

# Сортировка задач по дате добавления
# task_ids = [task.id for task in manager.queue]
# sorted_task = manager.bubble_sort(task_ids)
# sorted_tasks = sorted(manager.queue, key=lambda task: sorted_task.index(task.id))
#
# print("\nОтсортированный список ID задач:")
# for task in sorted_tasks:
#     print(f"ID: {task.id}, Задача: {task.description} дата: {task.time}")

# Асинхронное выполнение списка задач


# Использование асинхронное


# Использование асинхронное
# async def main():
#     semaphore = asyncio.Semaphore(3)
#     urls = ['https://www.example.com', 'https://www.python.org', 'https://www.wikipedia.org', 'https://github.com']
#     async with aiohttp.ClientSession() as session:
#         tasks = [process_url(session, url, semaphore) for url in urls]
#         results = await asyncio.gather(*tasks)
#         await save_results("links.json", results)
#
# asyncio.run(main())

# from sqlalchemy import (
#     Column, Integer, String, Text, ForeignKey, DECIMAL, TIMESTAMP, CheckConstraint, create_engine
# )
# from sqlalchemy.orm import relationship, Session
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime
# import warnings
# from sqlalchemy.schema import CreateTable
#
#
# warnings.filterwarnings("ignore")
# Base = declarative_base()
#
# class Category(Base): #категория задачи (встреча, звонок, дело)
#     __tablename__ = 'category'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False, unique=True)
#
#     # Связь с товарами
#     products = relationship("Типы задач", back_populates="category")
#
#     def __repr__(self):
#         return f"<Category(id={self.id}, name={self.name})>"
#


# Запуск нескольких задач одновременно
# import asyncio
#
# async def task(tasks_list, delay):
#     await asyncio.sleep(delay)
#     print(f'Task {tasks_list} completed')
#
#
# async def main():
#     for i, task in enumerate(tasks_list):
#         await asyncio.gather(lambda task_name=task, i=i: print(f"Задача {i + 1}: {task} выполнена"))
#         # manager.add_task(lambda task_name=task_name, i=i: print(f"Задача {i + 1}: {task_name} выполнена"))

    # await asyncio.gather(
    #     task('A', 2),
    #     task('B', 3),
    #     task('C', 1)
    # )

# asyncio.run(main())
#
# # for i, task_name in enumerate(tasks_list):  # Iterate through tasks with index
# #     manager.add_task(lambda task_name=task_name, i=i: print(f"Задача {i + 1}: {task_name} выполнена"))
# def main():
#     pass
#     add_category()
# if __name__ == "__main__":
#     main()

