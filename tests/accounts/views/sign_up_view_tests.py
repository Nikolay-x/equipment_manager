from django.contrib import auth
from django.test import TestCase
from django.urls import reverse


class SignUpViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'testuser',
        'email': 'testuser@email.com',
        'password1': 'QwertAsdf',
        'password2': 'QwertAsdf',
    }

    def test_sign_up__when_valid_data__expect_logged_in_user(self):
        self.client.post(
            reverse('profile signup'),
            self.VALID_USER_DATA,
        )

        user = auth.get_user(self.client)

        self.assertEqual(True, user.is_authenticated)
        self.assertEqual(self.VALID_USER_DATA['username'], user.username)
