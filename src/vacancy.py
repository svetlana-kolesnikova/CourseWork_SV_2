class Vacancy:
    #  __slots__
    def __init__(self, name, link, salary, desc):
        self.name = name
        self.link = link
        self.desc = desc
        self.__validate(salary)

    def __validate(self, salary):
        if salary:
            self.salary_from = salary['from'] if salary['from'] else 0
            self.salary_to = salary['to'] if salary['to'] else 0

        else:
            self.salary_from = 0
            self.salary_to = 0


    def __lt__(self, other):
        """<"""
        return self.salary_from < other.salary_from

    def __str__(self):
        return (f"Название: {self.name}\n"
                f"Ссылка: {self.link}\n"
                f"Описание: {self.desc}\n"
                f"Зарплата: от {self.salary_from} до {self.salary_to}\n")


if __name__ == '__main__':
    pass