from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, DECIMAL, TIMESTAMP, CheckConstraint, create_engine, DateTime
)
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import warnings
from sqlalchemy.schema import CreateTable

warnings.filterwarnings("ignore")
Base = declarative_base()

from idlelib.window import register_callback

import psycopg2

try:
    # Установить соединение с базой данных
    connection = psycopg2.connect(
        user="postgres",
        password="1234",
        host="127.0.0.1",
        port="5432",
        database="postgres"
    )
    print("Подключение к Базе данных успешно выполнено")

    cursor = connection.cursor()

    # создание таблицы списка задач
    # create_task_list = '''
    # CREATE TABLE tasks (
    #     id SERIAL PRIMARY KEY,
    #     name VARCHAR(100),
    #     date DATE
    # );
    # '''

    # cursor.execute(create_task_list)

    # Данные для вставки списка задач
    # insert_task: str = '''
    #     INSERT INTO tasks (name, date)
    #     VALUES (%s, NOW());
    #     '''
    # task_list = [
    #     ('Скачивание файла',),
    #     ('Обработка данных',),
    #     ('Резервное копирование',)
    # ]
    #
    # for task in task_list:
    #     cursor.execute(insert_task, task)
    # connection.commit()
    # print("Таблица 'task' успешно создана")
    # cursor.execute(insert_task, task_list)
    # connection.commit()
    # print("Таблица 'task' успешно создана")

# добавлена вторая часть задач
    insert_task: str = '''
        INSERT INTO tasks (name, date)
        VALUES (%s, NOW());
        '''
    task_list = [
        ('Синхронизация',),
        ('Анализ логов',),
        ('Экспорт данных',),
        ('Очистка кеша',),
        ('Обновление системы',),
        ('Мониторинг ресурсов',),
        ('Анализ логов',)
    ]

    for task in task_list:
        cursor.execute(insert_task, task)
    connection.commit()
    print("Задачи успешно добавлены")

except Exception as error:
    print("Ошибка при подключении к Базе данных", error)

finally:
    # Закрытие соединения
    if connection:
        connection.close()
        print("Соединение с PostgreSQL закрыто")
