from rest_framework import generics

from .models import Log
from .permissions import IsInitiatorOrReadOnly
from .serializers import LogSerializer


class LogList(generics.ListCreateAPIView):
    permission_classes = (IsInitiatorOrReadOnly,)
    queryset = Log.objects.all()
    serializer_class = LogSerializer


class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsInitiatorOrReadOnly,)
    queryset = Log.objects.all()
    serializer_class = LogSerializer
