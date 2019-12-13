from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from tradeit.models import Profile, Offer
from datetime import datetime


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
        page = Offer(offer_title="My Test Page", offer_description="test", pub_date=datetime.now())
        page.save()

        # Make sure the slug that was generated in Page.save()
        # matches what we think it should be.
        self.assertEqual(page.slug, "my-test-page")


class SamplesViewTests(TestCase):
    def test_samples_page(self):
        user = User.objects.create()
        offer = Offer.objects.create(offer_title="Something", offer_description="description of something", pub_date=datetime.now())
        response = self.client.get('/tradeit/')
        self.assertEqual(response.status_code, 200)
        response = response.context['offers']
        self.assertQuerysetEqual(
            response,
            ['<Offer: Something>']
        )
