from typing import List
from src.hh_api import HHApi
from src.json_saver import JsonSaver
from src.vacancy import Vacancy
from src.filters import filter_by_keyword


def main() -> None:
    """
    Основная функция взаимодействия с пользователем.
    Позволяет искать вакансии, показывать топ вакансий по зарплате,
    фильтровать вакансии по ключевому слову и выходить из программы.
    """
    print("Добро пожаловать в поисковик вакансий hh.ru!")
    api: HHApi = HHApi()
    saver: JsonSaver = JsonSaver()

    while True:
        print("\nВыберите действие:")
        print("1. Поиск вакансий по ключевому слову")
        print("2. Показать топ N вакансий по зарплате")
        print("3. Фильтр вакансий по ключевому слову в описании")
        print("4. Удаление вакансии по ссылке")
        print("5. Выход")

        choice: str = input("Введите номер действия: ").strip()
        if choice == "1":
            query: str = input("Введите ключевое слово для поиска вакансий: ").strip()
            print("Загружаю вакансии...")
            vacancies_raw: List[dict] = api.get_vacancies(query, page=2)  # можно менять количество страниц
            saver.write_vacancies(vacancies_raw)
            print(f"Найдено и сохранено {len(vacancies_raw)} вакансий.")

        elif choice == "2":
            try:

                n: int = int(input("Сколько вакансий показать? Введите число: ").strip())

            except ValueError:
                print("Введите корректное число.")

                continue

            currency_filter = (
                input("Введите код валюты (AZN, BYR, EUR, GEL, KGS, KZT, RUR, UAH, USD, UZS): ").strip().upper()
            )

            vacancies: List[Vacancy] = saver.read_vacancies()

            if not vacancies:
                print("Вакансии не загружены. Сначала выполните поиск.")

                continue

            # фильтруем по валюте

            filtered_by_currency = [vac for vac in vacancies if vac.currency == currency_filter]

            if not filtered_by_currency:
                print(f"Нет вакансий с валютой {currency_filter}")

                continue

            vacancies_sorted: List[Vacancy] = sorted(filtered_by_currency, reverse=True)

            top_n: List[Vacancy] = vacancies_sorted[:n]

            print(f"\nТоп {n} вакансий по зарплате в валюте {currency_filter}:")

            for vac in top_n:
                print(vac)

                print("-" * 40)

        elif choice == "3":
            keyword: str = input("Введите ключевое слово для фильтрации по описанию: ").strip()

            currency_filter = (
                input("Введите код валюты (AZN, BYR, EUR, GEL, KGS, KZT, RUR, UAH, USD, UZS): ").strip().upper()
            )

            vacancies: List[Vacancy] = saver.read_vacancies()

            if not vacancies:
                print("Вакансии не загружены. Сначала выполните поиск.")

                continue

            filtered: List[Vacancy] = filter_by_keyword(vacancies, keyword)

            # фильтрация по валюте

            filtered = [vac for vac in filtered if vac.currency == currency_filter]

            if not filtered:

                print(f"Вакансий с ключевым словом '{keyword}' и валютой '{currency_filter}' не найдено.")

            else:

                print(f"\nВакансии с ключевым словом '{keyword}' и валютой '{currency_filter}':")

                for vac in filtered:
                    print(vac)

                    print("-" * 40)

        elif choice == "4":
            link = input("Введите ссылку на вакансию для удаления: ").strip()
            saver.delete_vacancies(link)

        elif choice == "5":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
