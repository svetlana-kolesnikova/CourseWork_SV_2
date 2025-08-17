from typing import List
from src.vacancy import Vacancy
from src.filters import filter_by_salary, filter_by_keyword


def test_filter_by_salary() -> None:
    """
    Тест функции filter_by_salary.

    Проверяет, что:
    - вакансии с зарплатой выше или равной заданному минимуму включаются в результат;
    - вакансии с зарплатой ниже минимума или без зарплаты — исключаются.
    """
    v1: Vacancy = Vacancy("Dev", "link1", {"from": 50000, "to": 70000, "currency": "RUR"}, "Python")
    v2: Vacancy = Vacancy("Tester", "link2", {"from": 30000, "to": 40000, "currency": "RUR"}, "QA")
    v3: Vacancy = Vacancy("Manager", "link3", None, "Management")

    filtered: List[Vacancy] = filter_by_salary([v1, v2, v3], 40000)

    assert v1 in filtered
    assert v2 not in filtered
    assert v3 not in filtered


def test_filter_by_keyword() -> None:
    """
    Тест функции filter_by_keyword.

    Проверяет, что:
    - функция корректно фильтрует вакансии по ключевому слову в описании;
    - поиск не чувствителен к регистру.
    """
    v1: Vacancy = Vacancy("Dev", "link1", {"from": 50000, "to": 70000, "currency": "RUR"}, "Python")
    v2: Vacancy = Vacancy("Tester", "link2", {"from": 30000, "to": 40000, "currency": "RUR"}, "QA")

    result: List[Vacancy] = filter_by_keyword([v1, v2], "python")

    assert result == [v1]

