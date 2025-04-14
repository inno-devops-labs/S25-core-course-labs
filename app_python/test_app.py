import pytest
from app import app
from datetime import datetime
import pytz


@pytest.fixture
def client():
    """Создает тестовый клиент Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_homepage_status(client):
    """Проверяет, что главная страница возвращает код 200"""
    response = client.get('/')
    assert response.status_code == 200


def test_homepage_contains_moscow_time(client):
    """Проверяет, что главная страница содержит текущее московское время"""
    response = client.get('/')
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d')
    assert moscow_time in response.data.decode('utf-8')


def test_homepage_template(client):
    """Проверяет, что в шаблоне есть ключевые элементы"""
    response = client.get('/')
    data = response.data.decode('utf-8')
    assert "<h1>Current Time in Moscow</h1>" in data
    assert "The current time is:" in data
    assert "Refresh the page to update the time." in data


def test_invalid_route(client):
    """Проверяет, что несуществующая страница возвращает 404"""
    response = client.get('/invalid-page')
    assert response.status_code == 404
