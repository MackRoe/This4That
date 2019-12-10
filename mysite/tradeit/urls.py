from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('offer_list/', views.OfferList.as_view(), name="offer_list"),
    path('offer_detail/<slug>', views.OfferDetail.as_view(), name="offer_detail"),
]
