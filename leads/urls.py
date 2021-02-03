from django.urls import path
from .views import *
urlpatterns = [
    path('leads/', lead_page, name='lead-list'),
    path('leads/<int:pk>/', lead_detail, name='lead-detail'),
    path('leads/<int:pk>/update', lead_update, name='lead-update'),
    path('leads/<int:pk>/delete', lead_delete, name='lead-delete'),
    path('leads/create/', lead_create, name='lead-create'),
]