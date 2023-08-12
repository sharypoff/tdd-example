from datetime import datetime
from fastapi.testclient import TestClient
from freezegun import freeze_time
from .main import app

client = TestClient(app)


def test_my_info_success():
    initial_datetime = 1691377675
    with freeze_time(datetime.utcfromtimestamp(initial_datetime)):
        response = client.get("/my-info")
    assert response.status_code == 200
    result = {
        "user": {
            "id": 1,
            "firstname": "John",
            "lastname": "Smith",
            "phone": "+995000000000",
        },
        "timestamp": initial_datetime,
    }
    assert response.json() == result
    assert response.headers.get("X-Signature") == "479bb02f0f5f1249760573846de2dbc1"
