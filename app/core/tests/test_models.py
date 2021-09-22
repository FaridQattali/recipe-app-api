from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successfully(self):
        """Test that a user is created with email successfully!"""
        email = 'faridqattali@gmail.com'
        password = 'farid123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """ Checks that user email is normalized"""
        email = 'farid@MICROCIS.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, 'farid@microcis.com')

    def test_user_invalid_email(self):
        """Test a user without an email raises an error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        """Tests to create a superuser"""

        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
