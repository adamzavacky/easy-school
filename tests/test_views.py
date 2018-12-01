import pytest


@pytest.mark.django_db
class TestViews:

    def test_an_admin_view(self, admin_client):
        response = admin_client.get('/admin/')
        assert response.status_code == 200