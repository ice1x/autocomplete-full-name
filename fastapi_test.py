from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
EXPECTED = [
    {'name': 'александр', 'amount': '135746', 'gender': 'male', 'type': 'firstname'},
    {'name': 'александрович', 'amount': '129599', 'gender': 'male', 'type': 'middlename'},
    {'name': 'александровна', 'amount': '86711', 'gender': 'female', 'type': 'middlename'},
    {'name': 'андрей', 'amount': '84723', 'gender': 'male', 'type': 'firstname'},
    {'name': 'алексей', 'amount': '82645', 'gender': 'male', 'type': 'firstname'},
    {'name': 'анатольевич', 'amount': '68638', 'gender': 'male', 'type': 'middlename'},
    {'name': 'анатольевна', 'amount': '45446', 'gender': 'female', 'type': 'middlename'},
    {'name': 'алексеевич', 'amount': '42811', 'gender': 'male', 'type': 'middlename'},
    {'name': 'анна', 'amount': '30225', 'gender': 'female', 'type': 'firstname'},
    {'name': 'алексеевна', 'amount': '29105', 'gender': 'female', 'type': 'middlename'}
]


def test_read_main():
    response = client.get("/suggest/?query=%D0%B0&10")
    assert response.status_code == 200
    assert response.json() == EXPECTED


if __name__ == "__main__":
    test_read_main()

