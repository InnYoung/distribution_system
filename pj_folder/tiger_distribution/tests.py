from django.test import TestCase
from django.core.urlresolvers import resolve
from tiger_distribution.views import login_page


class LoginPageTest(TestCase):

    def test_get_login_page(self):
        response_login_page = resolve('/')
        self.assertEqual(response_login_page.func, login_page)
        