from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('profile_page/', views.profile_page, name="profile"),
    path('', views.OfferSampleView.as_view(), name="index"),
    path('offer_list/', views.OfferList.as_view(), name="offer_list"),
    path('offer_detail/<slug>', views.OfferDetail.as_view(), name="offer_detail"),
]
# not sure if that last comma belongs there
