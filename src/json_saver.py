import json
import os
from abc import ABC, abstractmethod
from typing import List

from src.vacancy import Vacancy


class AbstractJson(ABC):
    """
    Абстрактный класс для работы с файлами вакансий.
    """

    @abstractmethod
    def write_vacancies(self, vacancies: list[dict]) -> None:
        """
        Запись списка вакансий в файл.
        """
        pass

    @abstractmethod
    def read_vacancies(self) -> list[Vacancy]:
        """
        Чтение вакансий из файла.
        """
        pass

    @abstractmethod
    def delete_vacancies(self, link) -> None:
        """
        Удаление вакансий (заглушка).
        """
        pass


class JsonSaver(AbstractJson):
    """
    Класс для сохранения и чтения вакансий из JSON-файла.
    """

    def __init__(self, filename: str = "data/vacancies.json"):
        """
        Инициализация JsonSaver.
        """
        self.__filename = filename

    def write_vacancies(self, vacancies: List[dict]) -> None:
        """
        Записывает вакансии в JSON-файл, исключая дубли.
        """
        # Если файл не существует или пустой — инициализируем пустым списком
        if not os.path.exists(self.__filename) or os.path.getsize(self.__filename) == 0:
            vacancies_filter = []
        else:
            with open(self.__filename, encoding="utf-8") as fl:
                vacancies_filter = json.load(fl)

        # Собираем все существующие ссылки, чтобы избежать дубликатов
        existing_links = {v["link"] for v in vacancies_filter}

        # Добавляем только уникальные вакансии
        for vacancy in vacancies:
            if vacancy["alternate_url"] not in existing_links:
                description = vacancy.get("snippet", {}).get("requirement", "") or ""
                vacancies_filter.append(
                    {
                        "name": vacancy.get("name", ""),
                        "link": vacancy.get("alternate_url", ""),
                        "salary": vacancy.get("salary"),
                        "description": description,
                    }
                )

        # Сохраняем файл ОДИН раз
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(vacancies_filter, f, ensure_ascii=False, indent=4)

    def read_vacancies(self) -> List[Vacancy]:
        """
        Читает вакансии из JSON-файла и возвращает список объектов Vacancy.
        """
        with open(self.__filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [
            Vacancy(
                name=vacancy.get("name", ""),
                link=vacancy.get("link", ""),
                salary=vacancy.get("salary"),
                description=vacancy.get("description", ""),  # ← защита от None
            )
            for vacancy in data
        ]

    def delete_vacancies(self, link) -> None:
        """
        Удаляет вакансии из JSON-файла.

        Проверяет наличие файла, если файл существует, загружает данные,
        затем перезаписывает файл, исключая вакансии с определёнными условиями (например, по ссылке).
        В текущей реализации параметр для удаления не передаётся.
        """
        if not os.path.exists(self.__filename):
            print("Файл не найден.")
            return

        with open(self.__filename, encoding="utf-8") as f:
            data = json.load(f)

        new_data = [v for v in data if v["link"] != link]

        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)
