from django.contrib import admin

from .models import Profile
from .models import Offer
from .models import Contact
# Register your models here.
admin.site.register(Profile)
admin.site.register(Offer)
admin.site.register(Contact)
