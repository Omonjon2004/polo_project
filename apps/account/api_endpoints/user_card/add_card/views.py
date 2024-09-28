from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.account.api_endpoints.user_card.add_card.serializers import UserCardSerializer
from apps.account.models import UsersCards


class AddCardView(CreateAPIView):
    queryset = UsersCards.objects.all().order_by('id')
    serializer_class = UserCardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)

__all__ = ['AddCardView',]