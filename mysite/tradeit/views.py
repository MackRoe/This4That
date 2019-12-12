from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .models import Offer, Profile


def index(request):
    return HttpResponse("TradeIt index page")


def profile_page(request):
    model = Profile
    user = User.objects.get(pk=1)
    profile = Profile.objects.get(user=user)
    profile_context = {
        "profile": profile
    }

    return render(request, 'tradeit/profile.html', profile_context)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'tradeit/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


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


class OfferSampleView(ListView):
    '''Create an includible sample of offers for display on
    main page'''
    model = Offer

    def get(self, request):
        offer_context = {
            "offers": Offer.objects.all()[:4]
        }
        return render(request, "tradeit/samples.html", offer_context)
