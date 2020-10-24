from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from job_offer.models import JobOffer
from job_offer.api.serializers import JobOfferSerializer


class JobOfferDetailView(APIView):
    @staticmethod
    def get_object(pk):
        job_offer = get_object_or_404(JobOffer, pk=pk)
        return job_offer

    def get(self, request, pk):
        job_offer = self.get_object(pk=pk)
        serializer = JobOfferSerializer(job_offer)
        return Response(serializer.data)

    def put(self, request, pk):
        job_offer = self.get_object(pk=pk)
        serializer = JobOfferSerializer(job_offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        job_offer = self.get_object(pk=pk)
        job_offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JobOfferListCreateView(APIView):
    @staticmethod
    def get(request):
        job_offers = JobOffer.objects.all()
        serializer = JobOfferSerializer(job_offers, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
