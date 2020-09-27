from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/suggest/%D0%B0&10")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "амбарцумович", "amount": "99", "gender": "male", "type": "middlename"},
        {"name": "адгамович", "amount": "99", "gender": "male", "type": "middlename"},
        {"name": "авилов", "amount": "99", "gender": "male", "type": "lastname"},
        {"name": "аминова", "amount": "98", "gender": "female", "type": "lastname"},
        {"name": "алтухова", "amount": "98", "gender": "female", "type": "lastname"},
        {"name": "айшат", "amount": "98", "gender": "female", "type": "firstname"},
        {"name": "архипенко", "amount": "97", "gender": None, "type": "lastname"},
        {"name": "арапова", "amount": "97", "gender": "female", "type": "lastname"},
        {"name": "акчурина", "amount": "97", "gender": "female", "type": "lastname"},
        {"name": "арсеньева", "amount": "96", "gender": "female", "type": "lastname"}
    ]


if __name__ == "__main__":
    test_read_main()

