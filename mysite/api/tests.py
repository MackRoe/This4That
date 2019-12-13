from django.test import TestCase


# Create your tests here.
class TradeitApiCase(TestCase):
    def setUp(self):
        page = Offer(offer_title="My Test Page", offer_description="test 123")
        page.save()

    def test_api(self):
        test_offer = Offer.objects.get(offer_title="My Test Page")
        self.assertEqual(test_offer.offer_description, "test 123")
        self.assertEqual(test_offer.offer_title, "My Test Page")
