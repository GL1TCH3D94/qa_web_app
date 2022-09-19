from django.test import SimpleTestCase
from django.urls import reverse, resolve
from skill_matrix import views

class TestUrls(SimpleTestCase):
    
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, views.login_view)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, views.register_view)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, view.logout_view)