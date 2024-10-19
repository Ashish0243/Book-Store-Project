from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .views import HomePageView
class HomepageTests(SimpleTestCase):
    def setUp(self):
        url=reverse('home')
        self.response=self.client.get(url)
    
    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code,200)
        
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response,"homepage.html")
        
    def test_homepage_html_content(self):
        self.assertContains(self.response,"HOMEPAGE")
        
    def test_homepage_not_contain_html_content(self):
        self.assertNotContains(self.response,"hi there i am not supposed to be here.")
        
    def test_homepage_resolves_correct_view(self):
        view=resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )