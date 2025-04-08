import datetime
import time
import asyncio
from datetime import datetime
import random

# class Tasks: #паттерн Одиночка для списка задач
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(Tasks).__new__(cls)
#         return cls._instance
#
#     def __init__(self, task: str, id: int, data: time, status: str):
#         self.task = task
#         self.id = id
#         self.data = data
#         self.status = status
#
#     def __repr__(self):
#         return f"\n Задание:{self.id + 1}: {self.name, self.date}"
#
#     async def execute(self):
#         pass
#
#
# class GenerateID(Tasks): #Concrete Command
#     def __init__(self, id: int):
#         self.id = id
#     def execute(self):
#         self.generate_id()
#
# class GenerateData(Tasks): #Concrete Command
#     def __init__(self, data: time):
#         self.data = data
#
#     def execute(self):
#         self.generate_data()
#
# class Sorting(Tasks): #Concrete Command
#     def __init__(self, data: time):
#         self.data = data
#
#     def execute(self):
#         self.sorting()
#
# class Search(Tasks): #Concrete Command
#     def __init__(self, id: int):
#         self.id = id
#
#     def execute(self):
#         self.search()
#
#
# class AddTask(Tasks): #Concrete Command
#     def __init__(self, task: str, id: int, data: time):
#         self.task = task
#         self.id = id
#         self.data = data
#
#     def execute(self):
#         self.add_task()
#
# class DeleteTask(Tasks): #Concrete Command
#     def __init__(self, id: int):
#         self.id = id
#
#     def execute(self):
#         self.delete_task()
#
# class PrintList(Tasks): #Concrete Command
#     def __init__(self, task: str, id: int, data: time):
#         self.task = task
#         self.id = id
#         self.data = data
#
#     def execute(self):
#         self.print_list()
#
# class StartTask(Tasks):
#     def __init__(self, task: str, id: int, data: time):
#         self.task = task
#         self.id = id
#         self.data = data
#
#     def execute(self):
#         self.start_task()
#
#
# class Receiver(Tasks):
#     def generate_id(self):
#         while True:
#             id = random.randint(10000, 99999)  # Генерация номера из 5 чисел
#             if id not in Tasks:
#                 break
#
#     def generate_data(self):
#         data = datetime.datetime.now().strftime("%d.%m.%Y / %H.%M.%S")
#
#     def sorting(self):
#         def bubble_sort_task(Tasks):  # пузырьковая сортировка
#             n = len(Tasks)
#             for i in range(n):
#                 swapped = False
#                 for j in range(0, n - i - 1):
#                     if Tasks[j] > Tasks[j + 1]:
#                         Tasks[j], Tasks[j + 1] = Tasks[j + 1], Tasks[j]
#                         swapped = True
#                 if not swapped:
#                     break
#             return Tasks
#             print("\nСписок задач отсортированных по ID:")
#
#     def search(self): # линейный поиск по id
#         id_search = input("Введите ID задачи для поиска: ")
#         for task in Tasks:
#             if id == id_search:
#                 return id
#         return None
#
#
#     def add_task(self): # добавление новой задачи
#
#         new_task = input("Введите задачу: ")
#         new_id =random.randint(10000, 99999) if id not in Tasks else id
#         new_date = datetime.now()
#         new_task.append()
#         print(f"{new_date} - Задача '{new_task}' добавлена в список с ID: {new_id}")
#
#
#     def delete_task(self):
#         id_del = input("Введите номер задачи для удаления")
#         for d in Tasks if id != id_del else print("Задача не найдена"):
#             return Tasks.id.pop()
#         pass
#
#     def print_list(self):
#         for i in Tasks:
#             print(f"\n{Tasks.data} {Tasks.id} - Задача: {Tasks.task}")
#         pass
#
#     async def start_task(Tasks):
#         print(f"Задача {Tasks} запущена")
#         await asyncio.sleep(5)
#         print(f"Задача {Tasks} выполнена")
#
# async def task_start():
#     task = asyncio.gather(*Tasks)
#     await asyncio.sleep(5)
#
#     task.cancel()
#
# if __name__ == "__main__":
#
#
#     Task = [
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
#
#     task_list = Tasks()
#     manager = Receiver(Tasks)
#
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
#             asyncio.run(task_start)
#             print(f"Задача :{Tasks} выполнена")
#
#         elif choice == "6":
#             print("До свидания!")
#             break
#         else:
#             print(" Неверный ввод. Попробуйте снова.")
# -------

# class TaskManager:
#     _instance = None  # Singleton
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.tasks = []
#         return cls._instance
#
#     def add_task(self, command_func):
#         self.tasks.append(command_func)
#
#     def execute_all(self):
#         for task in self.tasks:
#             task()  # Вызов команды как функции
#         self.tasks.clear()
#
# # Использование
# manager = TaskManager()
#
# # Добавляем команды как обычные функции
# manager.add_task(lambda: print("Задача 1 выполнена"))
# manager.add_task(lambda: print("Задача 2 выполнена"))
#
# manager.execute_all()
#-----
# from abc import ABC, abstractmethod
#
# class Command(ABC):  # Абстрактный класс команды
#     @abstractmethod
#     def execute(self):
#         pass
#
# class TaskManager:
#     _instance = None  # Singleton
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.commands = []
#         return cls._instance
#
#     def add_command(self, command: Command):
#         self.commands.append(command)
#
#     def execute_all(self):
#         for cmd in self.commands:
#             cmd.execute()
#         self.commands.clear()
#
# # Конкретная команда
# class PrintCommand(Command):
#     def __init__(self, message):
#         self.message = message
#
#     def execute(self):
#         print(self.message)
#
# # Использование
# manager = TaskManager()
# manager.add_command(PrintCommand("Задача 1"))
# manager.add_command(PrintCommand("Задача 2"))
#
# manager.execute_all()
# ------

# class TaskManager:
#     _instance = None  # Singleton
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.tasks = []
#         return cls._instance
#
#     def add_task(self, command_func):
#         self.tasks.append(command_func)
#
#     def execute_all(self):
#         for task in self.tasks:
#             task()  # Вызов команды как функции
#         self.tasks.clear()
#
# # Использование
# manager = TaskManager()
#
# # Добавляем команды как обычные функции
# manager.add_task(lambda: print("Задача 1 выполнена"))
# manager.add_task(lambda: print("Задача 2 выполнена"))
#
# manager.execute_all()

# ------------

# Запуск нескольких задач одновременно
# import asyncio
#
# async def task(name, delay):
#     await asyncio.sleep(delay)
#     print(f'Task {name} completed')
#
# async def main():
#     await asyncio.gather(
#         task('A', 2),
#         task('B', 3),
#         task('C', 1)
#     )
#
# asyncio.run(main())

# _____
