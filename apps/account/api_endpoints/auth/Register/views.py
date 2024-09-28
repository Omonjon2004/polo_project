from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.account.api_endpoints.auth.Register.serializers import RegisterSerializer
from apps.account.models import Users


class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


__all__ = ['RegisterView',]
