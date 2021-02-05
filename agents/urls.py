from django.urls import path
from .views import *



urlpatterns = [
    path('agents/', AgentListView.as_view(), name='agent-list'),
    path('agents/create/', AgentCreateView.as_view(), name='agent-create'),
]
