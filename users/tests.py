from django.test import TestCase
from django.contrib.auth import get_user_model
class CusutomUserTests(TestCase):
    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(
            username="unknown1",
            email="unknown23@gmail.com",
            password="testpass123"
        )
        self.assertEqual(user.username,"unknown1")
        self.assertEqual(user.email,"unknown23@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        User=get_user_model()
        superuser=User.objects.create_superuser(
            username="superuser1",
            email="superuser1@gmail.com",
            password="testpass123"
        )
        self.assertEqual(superuser.username,"superuser1")
        self.assertEqual(superuser.email,"superuser1@gmail.com")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        
        
        
