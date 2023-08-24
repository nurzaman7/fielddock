from rest_framework import generics
from .models import Mission
from .serializers import MissionSerializer

class MissionListCreateView(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class MissionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

