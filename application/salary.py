from random import randint
from application.db.people import get_employees


def calculate_salary():
    hourly_rate = randint(150, 500)
    hours = randint(50, 220)
    for emp in get_employees():
        print(f'Заработная плата сотрудника {emp} составляет: {hourly_rate*hours} рублей')
