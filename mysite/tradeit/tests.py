from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from tradeit.models import Profile, Offer


class TradeitTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        # test may not work in current version
        """ Tests the slug generated when saving a Page. """
        # Author is a required field in our model.
        # Create a user for this test and save it to the test database.
        user = User()
        user_email = "@"
        user.save()

        # Create and save a new page to the test database.
        page = Offer(offer_title="My Test Page", offer_description="test")
        page.save()

        # Make sure the slug that was generated in Page.save()
        # matches what we think it should be.
        self.assertEqual(page.slug, "my-test-page")


class TradeitApiCase(TestCase):
    def setUp(self):
        page = Offer(offer_title="My Test Page", offer_description="test 123")
        page.save()

    def test_api(self):
        test_offer = Offer.objects.get(offer_title="My Test Page")
        self.assertEqual(test_offer.offer_description, "test 123")


class TradeitAccountsCase(TestCase):
    pass
