"""
Test for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
  """Test models"""

  def test_create_user_successful(self):
    """Test creating a user with an email is successful"""
    email = 'test@example.com'
    password = 'test123'
    user = get_user_model().objects.create_user(
      email=email,
      password=password,
    )

    self.assertEqual(user.email,email)
    self.assertTrue(user.check_password(password))
