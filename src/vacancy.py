class Vacancy:
    """
        Класс для представления вакансии.

        Атрибуты:
            name (str): Название вакансии.
            link (str): Ссылка на вакансию.
            desc (str): Краткое описание вакансии.
            salary_from (int): Нижняя граница зарплаты.
            salary_to (int): Верхняя граница зарплаты.
            currency (str): Валюта зарплаты.
        """
    __slots__ = ('name', 'link', 'desc', 'salary_from', 'salary_to', 'currency')

    def __init__(self, name: str, link: str, salary: dict, desc: str) -> None:
        """
                Инициализирует объект Vacancy.

                Args:
                    name (str): Название вакансии.
                    link (str): Ссылка на вакансию.
                    salary (dict): Словарь с информацией о зарплате.
                    desc (str): Описание вакансии.
                """
        self.name = name
        self.link = link
        self.desc = desc
        self.__validate(salary)

    def __validate(self, salary: dict | None) -> None:
        """
                Приватный метод для валидации зарплаты.

                Args:
                    salary (dict | None): Данные о зарплате.
                """
        if salary:
            self.currency = salary.get('currency', '')
            self.salary_from = salary.get('from') or salary.get('to') or 0
            self.salary_to = salary.get('to') or salary.get('from') or 0
        else:
            self.currency = ''
            self.salary_from = 0
            self.salary_to = 0

    def __lt__(self, other: 'Vacancy') -> bool:
        """
               Сравнение вакансий по зарплате (меньше).

               Args:
                   other (Vacancy): Другая вакансия для сравнения.

               Returns:
                   bool: Результат сравнения.
               """
        return self.salary_from < other.salary_from

    def __str__(self) -> str:
        """
                Строковое представление объекта.

                Returns:
                    str: Форматированная строка с информацией о вакансии.
                """
        return (f"Название: {self.name}\n"
                f"Ссылка: {self.link}\n"
                f"Описание: {self.desc}\n"
                f"Зарплата: от {self.salary_from} до {self.salary_to}, {self.currency}\n")


if __name__ == '__main__':
    pass
