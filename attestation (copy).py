from abc import ABC, abstractmethod
import uuid
from _datetime import datetime
from typing import Dict, List, Optional, Any
import asyncio
import random
from uuid import uuid4


# class Command(ABC):  # Абстрактный класс команды
#     def __init__(self, description):
#         self.id = str(uuid4())
#         self.description = description
#         self.time = datetime.now()
#
#     def __str__(self):
#         return f"Задача номер (ID={self.id}: '{self.description}', создана {self.time})"
#
#     @abstractmethod
#     def execute(self):
#         pass
#
#
# class TaskManager:
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.queue = []
#
#         return cls._instance
#
#     def add_task(self, task):
#         self.queue.append(task)
#         print(f'Задача {task.description} добавлена в очередь. Всего задач: {len(self.queue)}')
#
#     def bubble_sort(self, time):  # пузырьковая сортировка by adding time
#
#         n = len(time)
#         for i in range(n):
#             swapped = False
#             for j in range(0, n - i - 1):
#                 if time[j] > time[j + 1]:
#                     time[j], time[j + 1] = time[j + 1], time[j]
#                     swapped = True
#             if not swapped:
#                 break
#         return time
#         print("\nСписок задач отсортированных по времени:")
#
#     def linear_search(self, target):  # Линейный поиск id.
#         target = input(int("Введите ID задачи для поиска: "))
#         for task in Command:
#             if self.target == target:
#                 return target
#         return None
#
#     def delete_task(self, id):
#
#         for d in Command if id != target else print("Задача не найдена"):
#             return Command.id.pop()
#             print(f" Задача {id} удалена.")
#
#     def print_task_list(self, task=None):
#         if task:
#             print(f"{task}")
#         else:
#             for i, task in enumerate(self.queue, 1):
#                 print(f"{i}. {task}")
#
#     def execute_all(self):
#         pass
#         # for i in self.queue:
#         #     i.execute()
#         # self.queue.clear()
#
#     # async def execute_all(self):
#     #     for cmd in self.commands:
#     #         await asyncio.sleep(2
#     #         cmd.execute()
#     #     self.commands.clear()
#
#
# # Конкретные классы команд
# class PrintList(Command):
#     def __init__(self, description):
#         super().__init__(description)
#         self.description = description
#
#     def execute(self):
#         TaskManager().print_task_list(self)
#
#
# class AddTask(Command):
#     def __init__(self, *tasks):
#         self.tasks = tasks
#
#     def execute(self):
#         for task in self.tasks:
#             TaskManager().add_task()
#
#
# class BubbleSort(Command):  # класс для пузырьковой сортировки
#     def __init__(self, time):
#         self.time = time
#
#     def execute(self):
#         TaskManager().bubble_sort()
#
#
# class LinearSearch(Command):
#     def __init__(self, id):
#         self.id = id
#
#     def execute(self):
#         TaskManager().linear_search()
#
#
# class DeleteTask(Command):
#     def __init__(self, id):
#         self.id = id
#
#     def execute(self):
#         TaskManager().delete_task()
#
#
# # Использование
# manager = TaskManager()
#
# manager.add_task(PrintList("Скачивание файла"))
# manager.add_task(PrintList("Обработка данных"))
# manager.add_task(PrintList("Резервное копирование"))
# manager.add_task(PrintList("Синхронизация"))
# # manager.add_task(PrintList("Анализ логов"))
# # manager.add_task(PrintList("Экспорт данных"))
# # manager.add_task(PrintList("Импорт данных"))
# # manager.add_task(PrintList("Очистка кеша"))
# # manager.add_task(PrintList("Обновление системы"))
# # manager.add_task(PrintList("Мониторинг ресурсов"))
#
# manager.execute_all()
#
# # Печать списка задач
# print("\nСписок задач:")
# manager.print_task_list()
#
# manager.add_task(PrintList("Анализ логов"))
# manager.add_task(PrintList("Экспорт данных"))
# manager.add_task(PrintList("Импорт данных"))
# manager.add_task(PrintList("Очистка кеша"))
# manager.add_task(PrintList("Обновление системы"))
# manager.add_task(PrintList("Мониторинг ресурсов"))
# manager.execute_all()
# print("\nСписок задач:")
# manager.print_task_list()
#
# # Поиск задачи по ID
# manager.linear_search("40b52d0e-3611-4042-aaae-0e24103b3155")

# Удаление задачи по ID


#Сортировка задач по дате добавления

#
#_____

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
# class Incharge(Base): #ответственный за выполнение
#     __tablename__ = 'Ответственный'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     contact_info = Column(Text)
#
#     # Связь с поставками
#     shipments = relationship("Shipment", back_populates="supplier")
#
#     def __repr__(self):
#         return f"<Supplier(id={self.id}, name={self.name})>"
#
# # Модель для таблицы товаров
# class Product(Base):
#     __tablename__ = 'products'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     description = Column(Text)
#     quantity = Column(Integer, nullable=False, default=0)
#     category_id = Column(Integer, ForeignKey('categories.id'))
#     price = Column(DECIMAL(10, 2), nullable=False)
#     supplier_id = Column(Integer, ForeignKey('suppliers.id'))
#
#     # Связи
#     category = relationship("Category", back_populates="products")
#     transactions = relationship("Transaction", back_populates="product")
#     shipment_items = relationship("ShipmentItem", back_populates="product")
#
#     def __repr__(self):
#         return f"<Product(id={self.id}, name={self.name}, quantity={self.quantity}, price={self.price})>"


# старое
# import datetime
# import time
# import asyncio
# from datetime import datetime
# import random

# class TaskManager:
#     _instance = None  # Singleton

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.tasks = []
#         return cls._instance

#     def add_task(self, command_func):
#         self.tasks.append(command_func)

#     def execute_all(self):
#         for task in self.tasks:
#             task()  # Вызов команды как функции
#         self.tasks.clear()

# # Использование
# manager = TaskManager()

# Добавляем команды как обычные функции

# tasks_list = [
#         "Скачивание файла",
#         "Обработка данных",
#         "Синхронизация",
#         "Резервное копирование",
#         "Анализ логов",
#         "Экспорт данных",
#         "Импорт данных",
#         "Очистка кеша",
#         "Обновление системы",
#         "Мониторинг ресурсов",
#         ]


# for i, task_name in enumerate(tasks_list):  # Iterate through tasks with index
#     manager.add_task(lambda task_name=task_name, i=i: print(f"Задача {i + 1}: {task_name} выполнена"))



# manager.execute_all()


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

#_____

# Task = [
#         "Скачивание файла", 22153, "12.05.2025/13.44.24",
#         "Обработка данных", 23556, "29.03.2025 / 10.33.08",
#         "Синхронизация", 14576, "29.03.2025 / 11.02.00"
#         "Резервное копирование", 54321, "26.03.2025 / 15.02.01"
#         "Анализ логов", 98765, "30.03.2025 / 11.10.00"
#         "Экспорт данных", 13579, "30.03.2025 / 11.15.00"
#         "Импорт данных", 24680, "30.03.2025 / 11.06.00"
#         "Очистка кеша", 11223, "30.03.2025 / 11.08.00"
#         "Обновление системы", 44556, "30.03.2025 / 11.03.00"
#         "Мониторинг ресурсов", 77889, "30.03.2025 / 11.01.00"
#         ]