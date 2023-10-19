
from src.class_api import HeadHunterAPI, SuperJobAPI
from src.saving_vacancies import JSONVacancyStorage
from src.vacancy import Vacancy
def selects_platform():
    """Функция для выбора платформы"""
    storage = JSONVacancyStorage("vacancies.json")
    while True:
        platform_choice = input("Выберите платформу для поиска вакансий (1 - 'HeadHunter', 2 - 'SuperJob', 3 - 'Все платформы'): ")
        if platform_choice == '1':
            print("Отлично! Вы выбрали платформу 'HeadHunter' для поиска вакансий.")
            query = input("Введите запрос для поиска вакансий: ")
            print(f"Хорошо! Для поиска вы выбрали выбрали: '{query}' ")
            hh = HeadHunterAPI(query)
            hh_jobs = hh.get_jobs()
            json_vacancy_hh = storage.add_vacancy(hh_jobs)
            if storage.len_vacancy() == 0:
                print('К сожалению по данному запросу вакансий не найдено')
                continue
            return json_vacancy_hh
        elif platform_choice == '2':
            print("Отлично! Вы выбрали платформу 'SuperJob' для поиска вакансий.")
            query = input("Введите запрос для поиска вакансий: ")
            print(f"Хорошо! Для поиска вы выбрали выбрали: '{query}' ")
            sj = SuperJobAPI(query)
            sj_jobs = sj.get_jobs()
            json_vacancy_sj = storage.add_vacancy(sj_jobs)
            if storage.len_vacancy() == 0:
                print('К сожалению по данному запросу вакансий не найдено')
                continue
            return json_vacancy_sj
        elif platform_choice == '3':
            print("Отлично! Вы выбрали все платформы для поиска вакансий.")
            query = input("Введите запрос для поиска вакансий: ")
            print(f"Хорошо! Для поиска вы выбрали выбрали: '{query}' ")
            hh = HeadHunterAPI(query)
            sj = SuperJobAPI(query)
            hh_jobs = hh.get_jobs()
            sj_jobs = sj.get_jobs()
            all_jobs = hh_jobs + sj_jobs
            json_vacancy_all = storage.add_vacancy(all_jobs)
            if storage.len_vacancy() == 0:
                print('К сожалению по данному запросу вакансий не найдено')
                continue
            return json_vacancy_all
        else:
            print("Некорректный выбор платформы")




def searches_criteria():
    """Функция для поиска вакансий по региону"""
    storage = JSONVacancyStorage('vacancies.json')
    print("Введите регион для поиска вакансий (Например 'Москва')")
    print("Нажмите 'Enter' чтобы пропустить")
    criteria = input()
    if criteria != '':
        print(f"Хорошо! Для поиска вакансий Вы выбрали населенный пункт  - {criteria}")
        storage.get_vacancies(criteria)


#searches_criteria()

def sort_vacancy():
    """Сортирует вакансии по зарплате"""
    storage = JSONVacancyStorage('vacancies.json')
    vacancies = storage.load_vacancy()
    print(vacancies)
    vacancies = [Vacancy(**vacancy) for vacancy in vacancies]
    vacancies = sorted(vacancies)
    for vac in vacancies:
        print(vac)


