import pytest
from django import urls
from django.contrib.auth.models import User


#@pytest.mark.skip
@pytest.mark.django_db
def test_user_create_creates_profile():
    User.objects.create_user('michal', 'test@gmail.com', 'somepassword')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_jwt(client, created_user, login_data):
    url = urls.reverse('token_obtain_pair')
    response = client.post(url, login_data)
    assert response.status_code == 200
    assert 'access' and 'refresh' in response.data

    access_token = response.data['access']
    verification_url = urls.reverse('token_verify')
    resp = client.post(verification_url, {'token': access_token}, format='json')
    assert resp.status_code == 200
