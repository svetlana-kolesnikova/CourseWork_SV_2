class Vacancy:
    """
    Класс для представления вакансии.
    """

    __slots__ = ("name", "link", "desc", "salary_from", "salary_to", "currency", "description")

    def __init__(self, name: str, link: str, salary: dict, description: str) -> None:
        """
        Инициализирует объект Vacancy.
        """
        self.name = name
        self.link = link
        self.description = description
        self.__validate(salary)

    def __validate(self, salary: dict | None) -> None:
        """
        Приватный метод для валидации зарплаты.

        """
        if salary:
            self.currency = salary.get("currency", "")
            self.salary_from = salary.get("from") or salary.get("to") or 0
            self.salary_to = salary.get("to") or salary.get("from") or 0
        else:
            self.currency = ""
            self.salary_from = 0
            self.salary_to = 0

    def __lt__(self, other: "Vacancy") -> bool:
        """
        Сравнение вакансий по зарплате (меньше).
        """
        return self.salary_from < other.salary_from

    def __str__(self) -> str:
        """
        Строковое представление объекта.
        """
        return (
            f"Название: {self.name}\n"
            f"Ссылка: {self.link}\n"
            f"Описание: {self.description}\n"
            f"Зарплата: от {self.salary_from} до {self.salary_to}, {self.currency}\n"
        )


if __name__ == "__main__":
    pass
