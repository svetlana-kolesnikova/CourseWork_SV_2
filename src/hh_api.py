from abc import ABC, abstractmethod

import requests


class AbstractApi(ABC):
    """
    Абстрактный класс для работы с API сервиса вакансий.
    """

    @abstractmethod
    def _connect(self, text: str):
        """
        Подключение к API.
        """
        pass

    @abstractmethod
    def get_vacancies(self, text: str):
        """
        Получение вакансий по ключевому слову.
        """
        pass


class HHApi(AbstractApi):
    """
    Класс для работы с API hh.ru.
    """

    def __init__(self, page: int = 0):
        """
        Инициализация API.
        """
        self.__url = 'https://api.hh.ru/vacancies'
        self.__params = {'page': page, 'per_page': 30}

    def _connect(self, text: str):
        """
        Отправка запроса к API hh.ru.
        """
        self.__params['text'] = text
        response = requests.get(self.__url, self.__params)
        response.raise_for_status()
        return response

    def get_vacancies(self, text: str, page: int = 1):
        """
        Получение вакансий с hh.ru по ключевому слову.
        """
        all_vacancies = []
        while self.__params['page'] < page:
            vacancies = self._connect(text).json()['items']
            all_vacancies.extend(vacancies)
            self.__params['page'] += 1
        return all_vacancies


if __name__ == '__main__':
    hh = HHApi()
    print(hh.get_vacancies('python', 1))
