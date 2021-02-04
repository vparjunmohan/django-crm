from django.urls import path
from .views import *
urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('leads/', LeadListView.as_view(), name='lead-list'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('leads/<int:pk>/update', LeadUpdateView.as_view(), name='lead-update'),
    path('leads/<int:pk>/delete', LeadDeleteView.as_view(), name='lead-delete'),
    path('leads/create/', LeadCreateView.as_view(), name='lead-create'),
]
