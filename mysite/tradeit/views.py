from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Offer


def index(request):
    return HttpResponse("TradeIt index page")


class OfferList(ListView):
    model = Offer

    def get(self, request):
        offer_context = {
            "offers": Offer.objects.all()
        }
        return render(request, 'tradeit/offerlist.html', offer_context)
        pass


class OfferDetail(DetailView):
    model = Offer

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """
        page = Offer.objects.get(slug=slug)
        context = {
            "page": page
        }
        return render(request, "tradeit/offerdetail.html", context)
        pass

    def post(self, request, slug):
        pass
