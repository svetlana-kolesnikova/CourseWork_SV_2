from unittest.mock import MagicMock, patch

import pytest

from src.hh_api import HHApi


@patch("src.hh_api.requests.get")
def test_get_vacancies_success(mock_get: MagicMock) -> None:
    """
    Тестирует метод get_vacancies класса HHApi с использованием моков.

    Проверяет:
    - Корректную обработку данных, полученных от API hh.ru.
    - Постраничную загрузку (page > 1).
    - Что метод requests.get вызывается нужное количество раз.
    """
    # Создаём поддельный ответ от API
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = {
        "items": [
            {"name": "Python Developer", "alternate_url": "https://hh.ru/vacancy/1"},
            {"name": "Backend Developer", "alternate_url": "https://hh.ru/vacancy/2"},
        ]
    }
    mock_get.return_value = mock_response

    # Инициализация API и вызов метода
    api: HHApi = HHApi()
    vacancies: list[dict] = api.get_vacancies("python", page=2)

    # Проверки
    assert isinstance(vacancies, list)
    assert len(vacancies) == 4  # Две страницы по 2 вакансии каждая
    assert vacancies[0]["name"] == "Python Developer"
    assert mock_get.call_count == 2  # Проверка количества вызовов API
