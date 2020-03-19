from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.shortcuts import redirect


from .models import Offer, Profile
from .forms import UserForm, ProfileForm

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
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('/tradeit/profile_page')
        else:
            messages.error(request, 'Please correct the error below.')
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


class OfferListView(ListView):
    '''Create an includible sample of offers for display on
    main page'''
    model = Offer

    def get(self, request):
        offers = Offer.objects.all()[:4]
        offer_context = {
            "offers": offers
        }
        return render(request, "offer_list", offer_context)


class OfferCreate(CreateView):
    model = Offer
    fields = ['offer_title', 'offer_description', 'offer_maker', 'tokens_requested']
    success_url = reverse_lazy("offer_list")


class OfferUpdate(UpdateView):
    model = Offer
    fields = ['offer_title', 'offer_description', 'offer_maker', 'tokens_requested']
    success_url = reverse_lazy("tradeit/offerlist.html")


class OfferDelete(DeleteView):
    model = Offer
    success_url = reverse_lazy("tradeit/offerlist.html")
