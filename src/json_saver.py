from abc import ABC, abstractmethod


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
        vacancies_filter = []
        for vacancy in vacancies:
            vacancies_filter.append({'name': vacancy['name'], 'link': vacancy['alternate_url'], 'salary': vacancy['salary'], 'descryntion': vacancy['snipped']['requirement']})