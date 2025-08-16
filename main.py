from typing import List
from src.hh_api import HHApi
from src.json_saver import JsonSaver
from src.vacancy import Vacancy
from src.filters import filter_by_salary, filter_by_keyword  # твои вспомогательные функции


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
        print("4. Выход")
        print("5. Удаление вакансии по ссылке")


        choice: str = input("Введите номер действия: ").strip()

        if choice == '1':
            query: str = input("Введите ключевое слово для поиска вакансий: ").strip()
            print("Загружаю вакансии...")
            vacancies_raw: List[dict] = api.get_vacancies(query, page=2)  # можно менять количество страниц
            saver.write_vacancies(vacancies_raw)
            print(f"Найдено и сохранено {len(vacancies_raw)} вакансий.")

        elif choice == '2':
            try:
                n: int = int(input("Сколько вакансий показать? Введите число: ").strip())
            except ValueError:
                print("Введите корректное число.")
                continue

            vacancies: List[Vacancy] = saver.read_vacancies()
            if not vacancies:
                print("Вакансии не загружены. Сначала выполните поиск.")
                continue

            vacancies_sorted: List[Vacancy] = sorted(vacancies, reverse=True)
            top_n: List[Vacancy] = vacancies_sorted[:n]
            print(f"\nТоп {n} вакансий по зарплате:")
            for vac in top_n:
                print(vac)
                print('-' * 40)

        elif choice == '3':
            keyword: str = input("Введите ключевое слово для фильтрации по описанию: ").strip()
            vacancies: List[Vacancy] = saver.read_vacancies()
            if not vacancies:
                print("Вакансии не загружены. Сначала выполните поиск.")
                continue

            filtered: List[Vacancy] = filter_by_keyword(vacancies, keyword)
            if not filtered:
                print(f"Вакансий с ключевым словом '{keyword}' не найдено.")
            else:
                print(f"\nВакансии с ключевым словом '{keyword}':")
                for vac in filtered:
                    print(vac)
                    print('-' * 40)

        elif choice == '4':
            print("Выход из программы. До свидания!")
            break

        elif choice == '5':
            link = input("Введите ссылку на вакансию для удаления: ").strip()
            saver.delete_vacancies(link)


        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == '__main__':
    main()
