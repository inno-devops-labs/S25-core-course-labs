from unittest.mock import ANY
from datetime import datetime
from zoneinfo import ZoneInfo  

from freezegun import freeze_time

def test_ok_response(client):
    response = client.get('/')
    
    assert response.status_code == 200
    assert response.text == ANY

@freeze_time('2024-01-01 00:00:00')
def test_mocsow_template(client):
    response = client.get('/')
    
    assert response.status_code == 200
    assert response.text ==  f'<h1>Moscow time: 03:00:00</h1>'



@freeze_time('2024-01-01 00:00:00')
def test_mocsow_time_timezone(client):
    moscow_time = datetime.now(ZoneInfo('Europe/Moscow')).time()

    response = client.get('/')
    
    assert response.status_code == 200
    assert response.text == serialize_time(moscow_time)

def serialize_time(t: datetime) -> str:
    return f'<h1>Moscow time: {t}</h1>'