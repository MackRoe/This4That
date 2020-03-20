from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('profile_page/', views.profile_page, name="profile"),
    path('', views.OfferListView.as_view(), name="index"),
    path('offer_list/', views.OfferList.as_view(), name="offer_list"),
    path('offer_detail/<slug>', views.OfferDetail.as_view(), name="offer_detail"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('new_offer', views.OfferCreate.as_view(), name="new_offer"),
    path('update_offer/<slug>', views.OfferUpdate.as_view(), name="update_offer"),
    path('delete_offer/<slug>', views.OfferDelete, name="delete_offer"),
]
