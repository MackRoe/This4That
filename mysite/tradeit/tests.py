from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from wiki.models import Page


class WikiTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        # test may not work in current version
        """ Tests the slug generated when saving a Page. """
        # Author is a required field in our model.
        # Create a user for this test and save it to the test database.
        user_name = User()
        user_email = "@"
        user.save()

        # Create and save a new page to the test database.
        page = Offer(offer_title="My Test Page", offer_description="test")
        page.save()

        # Make sure the slug that was generated in Page.save()
        # matches what we think it should be.
        self.assertEqual(page.slug, "my-test-page")
