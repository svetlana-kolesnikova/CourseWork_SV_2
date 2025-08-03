from abc import ABC, abstractmethod

import requests



class AbstractApi(ABC):

    @abstractmethod
    def _connect(self, text):
        pass


    @abstractmethod
    def get_vacancies(self, text):
        pass


class HHApi(AbstractApi):
    def __init__(self, page=0):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__params = {'page': page, 'per_page': 30}


    def _connect(self, text):
        self.__params['text'] = text
        response = requests.get(self.__url, self.__params)
        response.raise_for_status()  # возвращает ошибку, если не "код ответа 200"
        return response

    def get_vacancies(self, text, page=0):
        all_vacancies = []
        while self.__params['page'] < page:
            vacancies = self._connect(text).json()['items']
            all_vacancies.extend(vacancies)
            self.__params['page'] += 1
        return all_vacancies


if __name__ == '__main__':
    hh = HHApi()
    print(hh.get_vacancies('python', 1))


