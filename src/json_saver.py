import json
import os
from abc import ABC, abstractmethod
from bisect import insort

from numpy.ma.core import inner

from src.vacancy import Vacancy


class AbstractJson(ABC):
    @abstractmethod
    def write_vacancies(self):
        pass

    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def delite_vacancies(self):
        pass

class JsonSaver(AbstractJson):
    def __init__(self, filename='data/vacancies.json'):
        self.__filename = filename

    def write_vacancies(self, vacancies: list[dict]):
        # Если файл не существует или пустой — инициализируем пустым списком
        if not os.path.exists(self.__filename) or os.path.getsize(self.__filename) == 0:
            vacancies_filter = []
        else:
            with open(self.__filename, encoding='utf-8') as fl:
                vacancies_filter = json.load(fl)

        # Собираем все существующие ссылки, чтобы избежать дубликатов
        existing_links = {v['link'] for v in vacancies_filter}

        # Добавляем только уникальные вакансии
        for vacancy in vacancies:
            if vacancy['alternate_url'] not in existing_links:
                vacancies_filter.append({
                    'name': vacancy['name'],
                    'link': vacancy['alternate_url'],
                    'salary': vacancy['salary'],
                    'description': vacancy['snippet']['requirement']
                })

        # Сохраняем файл ОДИН раз
        with open(self.__filename, 'w', encoding='utf-8') as f:
            json.dump(vacancies_filter, f, ensure_ascii=False, indent=4)


    def read_vacancies(self):
        with open(self.__filename, 'r', encoding='utf-8')as f:
            data = json.load(f)
        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(**vacancy))
            return vacancies

    def delite_vacancies(self):
        pass