from django.urls import path
from . import views

urlpatterns = [
    path('api/missions/', views.MissionListCreateView.as_view(), name='mission-list-create'),
    path('api/missions/<int:pk>/', views.MissionRetrieveUpdateDestroyView.as_view(), name='mission-retrieve-update-destroy'),
]

