# from datetime import datetime
# import datetime
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
#
# from datetime import datetime
# import datetime
# from typing import List, Optional
# import heapq
# import time
# from typing import List, Optional
# import heapq
# from datetime import time
# import json
# from collections import deque
# from queue import PriorityQueue

import asyncio
import uuid
from datetime import datetime

class Tasks: #класс с задачами
    def __init__(self, name: str, *args,**kwargs):
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
    except Exception as e:
        self.status = "failed"
        print(f"Ошибка при выполнении задачи {self.name}: {e}")
        raise

def __repr__(self):
    return (f"Task(id={self.id}, name={self.name}, "
            f"status={self.status}")

class Manager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        cls._instance = []
        return cls._instance

    def add_task(self, task: Tasks):#добавление новой задачи
        self.tasks.append(task)
        return task.id

    def search(self): #linear search by id
        pass

    def add_task(self): #add new task
        pass

    def delete_task(self): #delete task by id
        pass

    def sort_task(self): #sorting by choosing
        pass

    def bubble_sort(self): #sorting by datetime
        pass

    def view_task(self): #view the list of tasks
        pass

# async def execute_tasks(self, max_concurrent: int = 3) -> List[Task]: #async task doing
#
#     while self.tasks:
#             # Берем до max_concurrent задач
#         current_tasks = self.tasks[:max_concurrent]
#         self.tasks = self.tasks[max_concurrent:]
#
#             # Параллельное выполнение
#         results = await asyncio.gather(
#             *[task.execute() for task in current_tasks],
#             return_exceptions=True
#         )
#
#             # Обработка результатов
#         for task, result in zip(current_tasks, results):
#             if isinstance(result, Exception):
#                 print(f"Задача {task.name} завершилась с ошибкой: {result}")
#             else:
#                 self.completed_tasks.append(task)
#
#     return self.completed_tasks





#----- lesson asyncio----
# Асинхронная загрузка веб страниц
# async def fetch(session: aiohttp.ClientSession, url: str, semaphore: asyncio.Semaphore) -> Optional[str]:
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as response:
#                 return await response.text()
#     except:
#         print(f"Ошибка при загрузке {url}")
#------lesson asyncio end -----
#-------lesson patterns -----
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

# class Singleton:
#     """
#     Обычный класс с реализацией Singleton через атрибут класса.
#     """
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         """
#         Метод __new__ контролирует создание нового экземпляра.
#         Если объект уже существует, возвращает существующий.
#         """
#         if cls._instance is None:
#             cls._instance = super(Singleton, cls).__new__(cls)
#         return cls._instance
#
#     def __init__(self, value):
#         self.value = value
#
# # Пример использования:
# singleton1 = Singleton(42)
# singleton2 = Singleton(100)
#
# print(singleton1 is singleton2)  # Выведет: True
# print(singleton2.value)          # Выведет: 42, так как singleton2 ссылается на тот же объект

#------lesson patterns end-----


#-------------------------collab
# import uuid
# from datetime import datetime
# from dateutil import tz
#
# tasks = []
#
# def add_task():
#     task = input("Введите задачу: ")
#     task_id = uuid.uuid4()
#     now = datetime.now(tz=tz.tzlocal())
#     current_date_time = now.strftime("%Y-%m-%d %H:%M:%S %Z")
#     tasks.append({
#         "id": task_id,
#         "task": task,
#         "date_time": current_date_time
#     })
#     print(f"Задача '{task}' добавлена в список с ID: {task_id} и временем: {current_date_time}")
#
# def view_tasks():
#     if not tasks:
#         print("Список задач пуст.")
#     else:
#         for task in tasks:
#             print(f"ID: {task['id']}, Задача: {task['task']}, Дата и время: {task['date_time']}")
#
# while True:
#     action = input("Выберите действие (add/view/exit): ")
#     if action == "add":
#         add_task()
#     elif action == "view":
#         view_tasks()
#     elif action == "exit":
#         break
#     else:
#         print("Неверное действие. Попробуйте еще раз.")
#--------------------collab end-----

#--------from aatestation 1----
    # def remove_delivery(self, number: int):  # Удаляет поставку по номеру.
    #     self.deliveries = [d for d in self.deliveries if d.number != number]
    #     print(f" Доставка {number} удалена.")
#---------from attestetion1 end-----

#---------linear search from aatestation 1----
    # def linear_search(self, number: int) -> Optional[Delivery]:  # Линейный поиск доставки по номеру.
    #     for delivery in self.deliveries:
    #         if delivery.number == number:
    #             return delivery
    #     return None
#-------end linear search-----

#----- start process---
if __name__ == "__main__":
    orders = Orders()  # Создание начального списка заказов
    manager = DeliveryManager(orders)
    st = Stack()
    pq = DequeQueue()
    # d = Delivery()

    while True:
        print("\n Меню управления поставками:")
        print("1. Список заказов на доставку")
        print("2. Сортировать по номеру")
        print("3. Сортировать по весу груза")
        print("4. Сортировать по времени доставки")
        print("5. Найти доставку по номеру")
        print("6. Найти заказ по времени доставки")
        print("7. Добавить доставку")
        print("8. Удалить доставку")
        print("9. Изменить доставку")
        print("10. Отправка заказов \n(PS. Данный пункт работает частично, \nпонимаю как работает очередь и стек, \nно реализовать в коде до конца не смогла.\n 5 месяцев не хватило на более глубокое изучение)")
        print("11. Сохранить заказы в файл.")
        print("12. Выйти")

        choice = input("Введите номер команды: ")

        if choice == "1":
            print("\nСписок всех заказов:")
            manager.print_orders()

        elif choice == "2":
            sorted_delivery = manager.heap_sort(manager.deliveries, key_func=lambda delivery: delivery.number)
            print("\nСписок заказов отсортированных по номеру:")
            for delivery in sorted_delivery:
                print(delivery)


#----end start process---

#----sorting -----
# # сортировка выбором
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr
#
#
# result = selection_sort([29, 10, 14, 37, 13])
# print(result)
#---- end sorting----

#-----asyncio---
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
#----end asyncio----