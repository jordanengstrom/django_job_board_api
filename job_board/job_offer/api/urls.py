from django.urls import path
from job_offer.api.views import JobOfferListCreateView, JobOfferDetailView


urlpatterns = [
    path('joboffers/', JobOfferListCreateView.as_view(), name='job-offers-list'),
    path('joboffers/<int:pk>/', JobOfferDetailView.as_view(), name='job-offer-detail'),
]
