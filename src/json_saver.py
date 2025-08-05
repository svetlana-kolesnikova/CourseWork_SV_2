import json
from abc import ABC, abstractmethod
from bisect import insort

from numpy.ma.core import inner


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
        with open(self.__filename) as f:

            vacancies_filter = json.load(f)
            for vacancy in vacancies:
                if vacancy not in vacancies_filter:
                    vacancies_filter.append({
                        'name': vacancy['name'],
                        'link': vacancy['alternate_url'],
                        'salary': vacancy['salary'],
                        'description': vacancy['snippet']['requirement']
                    })

                with open(self.__filename, 'w', encoding='utf-8')as f:
                    json.dump(vacancies_filter, f, ensure_ascii=False, indent=4)


    def read_vacancies(self):
        pass

    def delite_vacancies(self):
        pass