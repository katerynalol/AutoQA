from employee_api import EmployeeApi


base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url) # Инициализация API-клиента

def test_create_employee():
    employee_json = {
            "first_name": "Kateryna",
            "last_name": "string",
            "middle_name": "string",
            "company_id": 2,
            "email": "user@example.com",
            "phone": "string",
            "birthdate": "2026-03-18",
            "is_active": True
    }
    new_employee = api.create_employ(data_json=employee_json)

    assert new_employee["first_name"] == "Kateryna"



def test_get_employee():
    employee_info = api.get_employee_by_id(1)

    assert employee_info["first_name"] == "Иван"


def test_edit_employee():
    mod_employee = api.edit_employee(1, "Mamoa", "harrypotter","expelliarmus")

    assert mod_employee["last_name"] == "Mamoa"

def test_edit_emptines_employee():
    mod_employee = api.edit_employee(1, "", "harrypotter","expelliarmus")

    assert mod_employee["last_name"] == ""