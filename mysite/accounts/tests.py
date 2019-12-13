from django.test import TestCase

from . import views, urls


# Create your tests here.
class TradeitAccountsCase(TestCase):
    def setUp(self):
        pass

    def test_accounts(self):
        self.AssertEqual(SignUp.template_name, 'signup.html')
        # self.AssertEqual()
