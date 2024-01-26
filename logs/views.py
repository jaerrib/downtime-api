from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Log
from .permissions import IsInitiatorOrReadOnly
from .serializers import LogSerializer, UserSerializer


class LogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsInitiatorOrReadOnly,)
    queryset = Log.objects.all()
    serializer_class = LogSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
