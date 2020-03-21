from django.contrib.auth.models import User
from accounts import forms
from .models import Profile, Offer, Contact


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'bio')


class NewOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('offer_maker', 'offer_title', 'offer_description', 'tokens_requested')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('sender_name', 'sender_email', 'sender_message_content')
