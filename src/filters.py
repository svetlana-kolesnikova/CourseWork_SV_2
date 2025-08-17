from src.vacancy import Vacancy


def filter_by_salary(vacancies: list[Vacancy], min_salary: int) -> list[Vacancy]:
    """
    Фильтрация вакансий по зарплате
    """
    return [vac for vac in vacancies if vac.salary_from >= min_salary]


def filter_by_keyword(vacancies: list[Vacancy], keyword: str) -> list[Vacancy]:
    """
    Фильтрация вакансий по ключевым словам
    """

    return [vac for vac in vacancies if vac.description and keyword.lower() in vac.description.lower()]
