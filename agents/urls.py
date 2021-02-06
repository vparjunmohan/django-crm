from django.urls import path
from .views import *



urlpatterns = [
    path('agents/<int:pk>/delete/', AgentDeleteView.as_view(), name='agent-delete'),
    path('agents/', AgentListView.as_view(), name='agent-list'),
    path('agents/create/', AgentCreateView.as_view(), name='agent-create'),
    path('agents/<int:pk>/', AgentDetailView.as_view(), name='agent-detail'),
    path('agents/<int:pk>/update/', AgentUpdateView.as_view(), name='agent-update'),
]
