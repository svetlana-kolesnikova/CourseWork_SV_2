from src.vacancy import Vacancy
from src.filters import filter_by_salary, filter_by_keyword

def test_filter_by_salary():
    v1 = Vacancy("Dev", "link1", {"from": 50000, "to": 70000, "currency": "RUR"}, "Python")
    v2 = Vacancy("Tester", "link2", {"from": 30000, "to": 40000, "currency": "RUR"}, "QA")
    v3 = Vacancy("Manager", "link3", None, "Management")
    filtered = filter_by_salary([v1, v2, v3], 40000)
    assert v1 in filtered
    assert v2 not in filtered
    assert v3 not in filtered

def test_filter_by_keyword():
    v1 = Vacancy("Dev", "link1", {"from": 50000, "to": 70000, "currency": "RUR"}, "Python")
    v2 = Vacancy("Tester", "link2", {"from": 30000, "to": 40000, "currency": "RUR"}, "QA")
    result = filter_by_keyword([v1, v2], "python")
    assert result == [v1]