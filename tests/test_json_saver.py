from src.json_saver import JsonSaver
from src.vacancy import Vacancy


def test_write_and_read_json(tmp_path) -> None:
    """
    Тестирует методы write_vacancies и read_vacancies класса JsonSaver.
    """
    test_file = tmp_path / "vacancies.json"
    saver = JsonSaver(str(test_file))

    vacancies = [
        {
            "name": "Backend Developer",
            "alternate_url": "http://example.com/job1",
            "salary": {"from": 80000, "to": 120000, "currency": "RUR"},
            "snippet": {"requirement": "Python, Django"},  # OK — так и нужно
        }
    ]

    saver.write_vacancies(vacancies)
    result = saver.read_vacancies()

    assert len(result) == 1
    assert isinstance(result[0], Vacancy)
    assert result[0].name == "Backend Developer"
    assert result[0].salary_from == 80000
