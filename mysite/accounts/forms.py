from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from tradeit.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    location = forms.CharField(max_length=250, required=False, help_text='Optional. Can be general or specific.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'location', 'email', 'password1', 'password2', )

#class UpdateProfileForm(UserChangeForm):
