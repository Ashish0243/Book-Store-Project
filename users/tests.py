from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve
from .forms import CustomUserCreationForm
from .views import SignUpView
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

class SignupPageTests(TestCase):
    def setUp(self):
        url=reverse('signup')
        self.response=self.client.get(url)
        
    def test_signup_templates(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'signup.html')
        self.assertContains(self.response,'SIGNUP')
        self.assertNotContains(self.response,'he he not supposed to be here ')
    
    def test_signup_form(self):
        form=self.response.context.get('form')
        self.assertIsInstance(form,CustomUserCreationForm)
        self.assertContains(self.response,"csrfmiddlewaretoken")
        
    def test_signup_view(self):
        view=resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignUpView.as_view().__name__
            
        )