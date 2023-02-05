import pytest
from faker import Faker

fake = Faker()


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def login_data():
    return {'username': fake.user_name(), 'password': fake.password()}


@pytest.fixture
def created_user(django_user_model, login_data):
    user_test = django_user_model.objects.create_user(**login_data)
    user_test.set_password(login_data.get('password'))
    return
