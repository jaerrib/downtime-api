from rest_framework import generics

from .models import Log
from .serializers import LogSerializer


class LogList(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer


class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
