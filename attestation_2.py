import datetime
# from typing import List, Optional
# import heapq
# import time
# from typing import List, Optional
# import heapq
# from datetime import time
# import json
# from collections import deque
# from queue import PriorityQueue
# import threading


import asyncio
import uuid
from datetime import datetime


class Tasks:  # класс с задачами, паттерн Команда
    def __init__(self, name: str, *args, **kwargs):
        self.name = name
        self.date = datetime.now()
        self.id = str(uuid.uuid4())
        self.status = "pending"
        self.result = None

    async def execute(self, task):
        try:
            self.status = "running"
            self.result = await self.action(*self.args, **self.kwargs)
            self.status = "completed"
            return self.result
        except:
            print(f"Ошибка при выполнении задачи {self.name}")

    def __repr__(self):
        return f"\n Задание:{self.id + 1}: {self.name, self.date}"


class Manager:  # паттерн Одиночка
    _instance = None

    def __new__(cls, *args, **kwargs):
        cls._instance = []
        return cls._instance

    def add_task(self, task: Tasks):  # добавление новой задачи

        self.tasks.append(task)
        new_task = input("Введите задачу: ")
        new_id = uuid.uuid4()
        new_date = datetime.now()
        new_task.append()
        print(f"{new_date} - Задача '{new_task}' добавлена в список с ID: {new_id}")

    def search(self, id):  # линейный поиск по id
        id_number = input("Введите ID задачи для поиска: ")
        for task in Tasks:
            if id == id_number:  # !!! id_number присвоить имя в запросе
                return id
        return None

    # def sort_task(self, task = Tasks(date)): #сортировка выбором
    #   for i in range(len(task)):
    #       min_idx = i
    #       for j in range(i + 1, len(task)):
    #         if task[j] < task[min_idx]:
    #             min_idx = j
    #       task[i], task[min_idx] = task[min_idx], task[i]

    #   return task
    # search_result = sort_task(self, task)

    # print("\nСписок задач отсортированных по ID:")
    # for i in search_result:
    #     print(f"{i}")

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

    def delete_task(self, id):  # удалить задачу по id
        id_del = input("Введите ID задачи: ")
        self.tasks = [datetime for datetime in self.tasks if id != id_del]
        print(f" Задача {id_del} удалена.")
        pass

    def view_task(self, task):  # показать список задач
        if not task():
            print("Список задач пуст.")
        else:
            print(f"ID: {task['id']}, Задача: {task['task']}, Дата и время: {task['date_time']}")

    def task_start():  # Запуск выполнения всех задач
        pass


async def main():
    tasks = Tasks()
    await asyncio.gather(*tasks)


# asyncio.run(main())
# print(f"Tasks are done. Amount :{}")

if __name__ == "__main__":

    # task_list = Tasks()
    manager = Manager()

    while True:
        print("\n Меню управления задачами:")
        print("1. Список задач по времени создания (метод сортировки - выбором)")
        print("2. Поиск задачи по ID (метод сортировки - линейный)")
        print("3. Добавить задачу")
        print("4. Удалить задачу")
        print("5. Запуск выполнения всех задач")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            print("\nСписок всех задач:")
            list = manager.view_task()

        elif choice == "2":
            sorted_tasks = manager.bubble_sort_task(manager.task, key_func=lambda task: task.id)
            result = manager.bubble_sort_task(id)
            print(result if result else "Задача не найдена.")

        elif choice == "3":
            add_new_task = manager.add_task()

        elif choice == "4":
            delete_task = manager.delete_task()

        elif choice == "5":
            start_tasks = manager.task_start()

        elif choice == "6":
            print("До свидания!")
            break
        else:
            print(" Неверный ввод. Попробуйте снова.")

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