from src.vacancy import Vacancy


def test_salary_validation_full_data() -> None:
    """
    Проверяет правильную инициализацию зарплаты при полном словаре.
    """
    salary = {"from": 100000, "to": 150000, "currency": "RUR"}
    v = Vacancy("Python Dev", "http://example.com", salary, "description")
    assert v.salary_from == 100000
    assert v.salary_to == 150000
    assert v.currency == "RUR"


def test_salary_validation_only_from() -> None:
    """
    Проверяет инициализацию, если указан только 'from'.
    """
    salary = {"from": 70000, "currency": "RUR"}
    v = Vacancy("Frontend Dev", "http://example.com", salary, "description")
    assert v.salary_from == 70000
    assert v.salary_to == 70000  # Дублируется значение from
    assert v.currency == "RUR"


def test_salary_validation_only_to() -> None:
    """
    Проверяет инициализацию, если указан только 'to'.
    """
    salary = {"to": 50000, "currency": "USD"}
    v = Vacancy("Intern", "http://example.com", salary, "description")
    assert v.salary_from == 50000
    assert v.salary_to == 50000
    assert v.currency == "USD"


def test_missing_salary() -> None:
    """
    Проверяет поведение при отсутствии словаря зарплаты (None).
    """
    v = Vacancy("QA", "http://example.com", None, "description")
    assert v.salary_from == 0
    assert v.salary_to == 0
    assert v.currency == ""


def test_str_representation() -> None:
    """
    Проверяет строковое представление объекта Vacancy.
    """
    salary = {"from": 60000, "to": 90000, "currency": "RUR"}
    v = Vacancy("Data Analyst", "http://example.com", salary, "Excel, SQL")
    result = str(v)
    assert "Название: Data Analyst" in result
    assert "Ссылка: http://example.com" in result
    assert "Описание: Excel, SQL" in result
    assert "Зарплата: от 60000 до 90000, RUR" in result


def test_comparison_lt_true() -> None:
    """
    Проверяет сравнение двух вакансий — одна меньше по зарплате.
    """
    v1 = Vacancy("Junior", "url1", {"from": 50000}, "desc")
    v2 = Vacancy("Middle", "url2", {"from": 80000}, "desc")
    assert v1 < v2


def test_comparison_lt_false() -> None:
    """
    Проверяет сравнение — результат False, если зарплата выше.
    """
    v1 = Vacancy("Senior", "url1", {"from": 120000}, "desc")
    v2 = Vacancy("Middle", "url2", {"from": 80000}, "desc")
    assert not (v1 < v2)
