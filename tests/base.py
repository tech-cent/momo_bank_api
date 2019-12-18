from rest_framework.test import APITestCase
from django.urls import reverse

class BaseTestCase(APITestCase):
    """
    All helper methods
    """

    def signup_user(self, user):
        """
        Method signups user it is given
        by sending post request to signup
        endpoint
        """
        url = reverse('authentication:signup')
        return self.client.post(url, user, format='json')
