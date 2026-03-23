# Разработать автоматические тесты, которые проверяют корректность работы API для управления сотрудниками.
# Создайте класс EmployeeApi для создания вспомогательных методов.
# API Методы
# 1. Создание нового работника
# Метод: POST
# URL: http://5.101.50.27:8000/employee/create
# Описание: Создаёт нового сотрудника, принимает данные в JSON.

import requests

class EmployeeApi:
    """Класс для взаимодействия с API компаний"""

    def __init__(self, url):
        """Инициализация класса с базовым URL API"""
        self.url = url

    def create_employ(self, data_json):
        """Получить список всех компаний"""
        resp = requests.post(self.url + '/employee/create', json=data_json)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_employee_by_id(self, id):
        resp = requests.get(self.url + f'/employee/info/{id}')
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()



    def get_token(self, user, password):
        """Получить токен авторизации"""
        creds = {"username": user, "password": password}
        resp = requests.post(self.url + '/auth/login', json=creds)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()["user_token"]

    def edit_employee(self, employee_id, last_name, user, password):
        """Изменить название и описание компании по ID"""
        client_token = self.get_token(user, password)
        url_with_token = f"{self.url}/employee/change/{employee_id}?client_token={client_token}"

        employee_data = {
            "last_name": last_name
        }
        resp = requests.patch(url_with_token, json=employee_data)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()