import datetime
# from typing import List, Optional
# import heapq
import time
# from typing import List, Optional
# import heapq
# from datetime import time
# import json
# from collections import deque
# from queue import PriorityQueue
# import threading


import asyncio
import uuid
from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK
from datetime import datetime
from abc import ABC, abstractmethod
import random
from gc import is_finalized


class Tasks: #паттерн Одиночка для списка задач
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Tasks).__new__(cls)
        return cls._instance

    def __init__(self, task: str, id: int, data: time):
        self.task = task
        self.id = id
        self.data = data

    def execute(self):
        pass

# class Command(ABC): #абстрактный класс запускающий операции
#     @abstractmethod
#     def execute(self):
#         pass

class GenerateID(Tasks): #Concrete Command
    def __init__(self, id: int):
        self.id = id
    def execute(self):
        self.generate_id()

class GenerateData(Tasks): #Concrete Command
    def __init__(self, data: time):
        self.data = data

    def execute(self):
        self.generate_data()

class Sorting(Tasks): #Concrete Command
    def __init__(self, data: time):
        self.data = data

    def execute(self):
        self.sorting()

class Search(Tasks): #Concrete Command
    def __init__(self, id: int):
        self.id = id

    def execute(self):
        self.search()


class AddTask(Tasks): #Concrete Command
    def __init__(self, task: str, id: int, data: time):
        self.task = task
        self.id = id
        self.data = data

    def execute(self):
        self.add_task()

class DeleteTask(Tasks): #Concrete Command
    def __init__(self, id: int):
        self.id = id

    def execute(self):
        self.delete_task()

class PrintList(Tasks): #Concrete Command
    def __init__(self, task: str, id: int, data: time):
        self.task = task
        self.id = id
        self.data = data

    def execute(self):
        self.print_list()

class Receiver(Tasks):
    def generate_id(self):
        while True:
            id = random.randint(10000, 99999)  # Generate a 5-digit number
            if id not in Tasks:  # Check for uniqueness
                break

    def generate_data(self):
        data = datetime.datetime.now().strftime("%d.%m.%Y / %H.%M.%S")

    def sorting(self):
        def bubble_sort_task(Tasks):  # пузырьковая сортировка
            n = len(Tasks)
            for i in range(n):
                swapped = False
                for j in range(0, n - i - 1):
                    if Tasks[j] > Tasks[j + 1]:
                        Tasks[j], Tasks[j + 1] = Tasks[j + 1], Tasks[j]
                        swapped = True
                if not swapped:
                    break
            return Tasks
            print("\nСписок задач отсортированных по ID:")

    def search(self): # линейный поиск по id
        id_search = input("Введите ID задачи для поиска: ")
        for task in Tasks:
            if id == id_search:
                return id
        return None


    def add_task(self): # добавление новой задачи

        new_task = input("Введите задачу: ")
        new_id =random.randint(10000, 99999) if id not in Tasks else id
        new_date = datetime.now()
        new_task.append()
        print(f"{new_date} - Задача '{new_task}' добавлена в список с ID: {new_id}")


    def delete_task(self):
        id_del = input("Введите номер задачи для удаления")
        for d in Tasks if id != id_del else print("Задача не найдена"):
            return Tasks.id.pop()
        pass

    def print_list(self):
        for i in Tasks:
            print(f"\n{Tasks.data} {Tasks.id} - Задача: {Tasks.task}")
        pass

# class Tasks: # класс с задачами, паттерн Команда
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(tasks, cls).__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         self.tasks = []
#
#
#
#
#
#     async def execute(self, task):
#         try:
#             self.status = "running"
#             self.result = await self.action(*self.args, **self.kwargs)
#             self.status = "completed"
#             return self.result
#         except:
#             print(f"Ошибка при выполнении задачи {self.name}")
#
#     def __repr__(self):
#         return f"\n Задание:{self.id + 1}: {self.name, self.date}"
#
#
# class Manager:  # паттерн Одиночка
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         cls._instance = []
#         return cls._instance
#
#     # def add_task(self, task: Tasks):  # добавление новой задачи
#     #
#     #     self.tasks.append(task)
#     #     new_task = input("Введите задачу: ")
#     #     new_id = uuid.uuid4()
#     #     new_date = datetime.now()
#     #     new_task.append()
#     #     print(f"{new_date} - Задача '{new_task}' добавлена в список с ID: {new_id}")
#
#     def search(self, id):  # линейный поиск по id
#         id_number = input("Введите ID задачи для поиска: ")
#         for task in Tasks:
#             if id == id_number:
#                 return id
#         return None
#     def add_tasks(self):
#         new_task = input("Введите задачу: ")
#         new_id = if task_number not in [task["number"] for task in tasks]
#         new_date = datetime.now()
#         new_task.append()
#         print(f"{new_date} - Задача '{new_task}' добавлена в список с ID: {new_id}")
#
#     def delete_tasks(self, id): # удалить задачу по id
#
#         self.tasks = [d for d in self.tasks if id != id_del]
#         return self.id.pop()

#     # def sort_task(self, task = Tasks(date)): #сортировка выбором
#     #   for i in range(len(task)):
#     #       min_idx = i
#     #       for j in range(i + 1, len(task)):
#     #         if task[j] < task[min_idx]:
#     #             min_idx = j
#     #       task[i], task[min_idx] = task[min_idx], task[i]
#
#     #   return task
#     # search_result = sort_task(self, task)
#
#     # print("\nСписок задач отсортированных по ID:")
#     # for i in search_result:
#     #     print(f"{i}")
#
#     def bubble_sort_task(Tasks):  # пузырьковая сортировка
#         n = len(Tasks)
#         for i in range(n):
#             swapped = False
#             for j in range(0, n - i - 1):
#                 if Tasks[j] > Tasks[j + 1]:
#                     Tasks[j], Tasks[j + 1] = Tasks[j + 1], Tasks[j]
#                     swapped = True
#             if not swapped:
#                 break
#         return Tasks
#         print("\nСписок задач отсортированных по ID:")
#
#     def delete_task(self, id):  # удалить задачу по id
#         id_del = input("Введите ID задачи: ")
#         self.tasks = [datetime for datetime in self.tasks if id != id_del]
#         print(f" Задача {id_del} удалена.")
#         pass
#
#     def view_task(self, task):  # показать список задач
#         if not task():
#             print("Список задач пуст.")
#         else:
#             print(f"ID: {task['id']}, Задача: {task['task']}, Дата и время: {task['date_time']}")
#
#     async def task_start():  # Запуск выполнения всех задач
#         tasks = Tasks()
#         await asyncio.gather(*tasks)
#
#
# if __name__ == "__main__":
#
#     tasks = {
#         "Номер": 23556,
#         "Задача": "Открыть папку",
#         "Дата, время": "29.03.2025 / 10.33.08"
#     }
#
#     task_list = Tasks()
#     manager = Manager()
#
#     while True:
#         print("\n Меню управления задачами:")
#         print("1. Список задач по времени создания (метод сортировки - выбором)")
#         print("2. Поиск задачи по ID (метод сортировки - линейный)")
#         print("3. Добавить задачу")
#         print("4. Удалить задачу")
#         print("5. Запуск выполнения всех задач")
#         print("6. Выход")
#
#         choice = input("Введите номер действия: ")
#
#         if choice == "1":
#             print("\nСписок всех задач:")
#             list = manager.view_task()
#
#         elif choice == "2":
#             sorted_tasks = manager.bubble_sort_task(manager.task, key_func=lambda task: task.id)
#             result = manager.bubble_sort_task(id)
#             print(result if result else "Задача не найдена.")
#
#         elif choice == "3":
#             add_new_task = manager.add_task()
#
#         elif choice == "4":
#             id_del = input("Введите ID задачи: ")
#             delete_task = manager.delete_tasks()
#             print(f" Задача {id_del} удалена.")
#
#         elif choice == "5":
#             start_tasks = manager.task_start()
#             print(f"Tasks are done. Amount :{}")
#
#         elif choice == "6":
#             print("До свидания!")
#             break
#         else:
#             print(" Неверный ввод. Попробуйте снова.")

# ----- lesson asyncio----
# Асинхронная загрузка веб страниц
# async def fetch(session: aiohttp.ClientSession, url: str, semaphore: asyncio.Semaphore) -> Optional[str]:
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as response:
#                 return await response.text()
#     except:
#         print(f"Ошибка при загрузке {url}")
# ------lesson asyncio end -----
# -------lesson patterns -----
# главная функция
# async def main():
#     semaphore = asyncio.Semaphore(3)
#     urls = ['https://www.example.com', 'https://www.python.org', 'https://www.wikipedia.org', 'https://github.com']
#     async with aiohttp.ClientSession() as session:
#         tasks = [process_url(session, url, semaphore) for url in urls]
#         results = await asyncio.gather(*tasks)
#         await save_results("links.json", results)
#
# asyncio.run(main())


# -----asyncio---
# import asyncio
#
# counter = 0
# lock = asyncio.Lock()
#
# class HotelLUX:
#     def __init__(self, room_lux: str = "LUX Room", price_lux: int = 100):
#         self.room_lux = room_lux
#         self.price_lux = price_lux
#
# class Hotel:
#     def __init__(self, room: str = "Standart room", price: int = 50):
#         self.room = room
#         self.price = price
#
# async def sell_lux_rooms():
#     l = HotelLUX()
#     global counter
#     for _ in range(15):
#         async with lock:
#             counter += l.price_lux
#
# async def sell_rooms():
#     h = Hotel()
#     global counter
#     for _ in range(20):
#         async with lock:
#             counter+= h.price
#
# async def main():
#     tasks = [sell_rooms(), sell_lux_rooms()]
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())
# print(f"Номера в обоих отелях забронировали на сумму: {counter}")
# ----end asyncio----