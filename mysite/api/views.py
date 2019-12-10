from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from tradeit.models import Profile, Offer
from api.serializers import OfferSerializer
from api.serializers import ProfileSerializer


class OfferList(APIView):
    def get(self, request):
        offers = Offer.objects.all()[:20]
        data = OfferSerializer(offers, many=True).data
        return Response(data)


class OfferDetail(APIView):
    def get(self, request, pk):
        offer = get_object_or_404(Offer, pk=pk)
        data = OfferSerializer(question).data
        return Response(data)
