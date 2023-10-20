from src.class_api import HeadHunterAPI, SuperJobAPI
from src.saving_vacancies import JSONVacancyStorage
from src.vacancy import Vacancy


def selects_platform():
    """Функция для выбора платформы"""

    storage = JSONVacancyStorage("vacancies.json")

    while True:
        platform_choice = input("Выберите платформу для поиска вакансий (1 - 'HeadHunter', 2 - 'SuperJob', 3 - 'Все платформы'): ").strip()
        if platform_choice == '1':
            print("Отлично! Вы выбрали платформу 'HeadHunter' для поиска вакансий.")
            query = input("Введите запрос для поиска вакансий: ")
            print(f"Хорошо! Для поиска вы  выбрали: '{query}'")
            hh = HeadHunterAPI(query)
            hh_jobs = hh.get_jobs()
            json_vacancy_hh = storage.add_vacancy(hh_jobs)
            if storage.len_vacancy() == 0:
                print('К сожалению по данному запросу вакансий не найдено.')
                print("Попробуйте еще раз!")
                continue
            return json_vacancy_hh
        elif platform_choice == '2':
            print("Отлично! Вы выбрали платформу 'SuperJob' для поиска вакансий.")
            query = input("Введите запрос для поиска вакансий: ")
            print(f"Хорошо! Для поиска вы выбрали: '{query}'")
            sj = SuperJobAPI(query)
            sj_jobs = sj.get_jobs()
            json_vacancy_sj = storage.add_vacancy(sj_jobs)
            if storage.len_vacancy() == 0:
                print('К сожалению по данному запросу вакансий не найдено.')
                print("Попробуйте еще раз!")
                continue
            return json_vacancy_sj
        elif platform_choice == '3':
            print("Отлично! Вы выбрали все платформы для поиска вакансий.")
            query = input("Введите запрос для поиска вакансий: ")
            print(f"Хорошо! Для поиска вы выбрали: '{query}'")
            hh = HeadHunterAPI(query)
            sj = SuperJobAPI(query)
            hh_jobs = hh.get_jobs()
            sj_jobs = sj.get_jobs()
            all_jobs = hh_jobs + sj_jobs
            json_vacancy_all = storage.add_vacancy(all_jobs)
            if storage.len_vacancy() == 0:
                print('К сожалению по данному запросу вакансий не найдено.')
                print("Попробуйте еще раз!")
                continue
            return json_vacancy_all
        else:
            print("Некорректный выбор платформы.")
            print("Попробуйте еще раз!")


def searches_criteria():
    """Функция для поиска вакансий по региону"""

    while True:
        storage = JSONVacancyStorage('vacancies.json')
        print("Введите регион для поиска вакансий (Например 'Санкт-Петербург')")
        print("Или нажмите 'Enter' чтобы пропустить")
        criteria = input().strip(" .").title()
        if criteria != '':
            print(f"Хорошо! Для поиска вакансий Вы выбрали населенный пункт  - {criteria}")
            storage.get_vacancies(criteria)
            if storage.len_vacancy() == 0:
                print(f"К сожалению в населенном пункте '{criteria}' вакансий не найдено!")
        break


def sort_vacancy():
    """Сортирует вакансии по зарплате от меньшего к большему"""

    storage = JSONVacancyStorage('vacancies.json')
    vacancies = storage.load_vacancy()
    vacancies = [Vacancy(**vacancy) for vacancy in vacancies]
    vacancies = sorted(vacancies, reverse=True)
    return vacancies


def top_vacanсy():
    """Выводит top-n вакансий по зарплате"""

    while True:
        print("Хотите получить топ-N вакансий по зарплате?")
        print("Введите 'Да', если хотите получить топ-N вакансий по зарплате.")
        print("Или нажмите 'Enter', чтобы пропустить данный шаг.")
        user_input = input().title()
        if user_input == 'Да':
            storage = JSONVacancyStorage('vacancies.json')
            vacancies = storage.load_vacancy()
            vacancies = [Vacancy(**vacancy) for vacancy in vacancies]
            print("Введите количество вакансий для топ-N по зарплате (Например: 5)")
            try:
                user_num = int(input())
                if 1 <= user_num <= storage.len_vacancy():
                    print(f"Отлично! Вот топ - {user_num} вакансий по зарплате от большего к меньшему: ")
                    vacancies = sorted(vacancies, key=lambda x: x.salary_from, reverse=True)[:user_num]
                    for vac in vacancies:
                        print(repr(vac) + '\n')
                    break
                else:
                    print("Некорректное значение")
            except ValueError:
                print("Некорректный ввод, введите целое число")
        elif user_input.strip() == '':
            return False
        else:
            print("Некорректный ввод, повторите попытку")