from pickle import FALSE

from django.template.context_processors import request
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.account.api_endpoints.auth.profile.serializers import UserSerializer
from apps.account.models import Users


class ProfileViewSet(viewsets.ViewSet):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    @action(methods=["get"], detail=False)
    def user_profile(self, *args, **kwargs):
        account = Users.objects.get(pk=self.request.user.id)
        serializer = UserSerializer(account)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        account =get_object_or_404(Users, pk=self.request.user.id)
        original_email = account.email
        serializer = UserSerializer(account, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if 'email' in serializer.validated_data and serializer.validated_data['email'] != original_email:
            account.is_active = False

        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        account = get_object_or_404(Users, pk=self.request.user.id)
        self.perform_destroy(account)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    @action(methods=["post"], detail=False)
    def account_exit(self, *args, **kwargs):
        account = get_object_or_404(Users, pk=self.request.user.id)
        account.is_active = False
        account.save()
        return Response(status=status.HTTP_200_OK)





__all__ = ["ProfileViewSet",]
