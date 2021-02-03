from django.urls import path
from .views import *
urlpatterns = [
    path('leads/', lead_page, name='leads'),
    path('leads/<pk>/', lead_detail, name='lead_detail'),
]