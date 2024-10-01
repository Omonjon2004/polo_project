from rest_framework.generics import ListCreateAPIView

from apps.product.api_endpoints.dress.serializers import DressSerializer
from apps.product.models import Dress


class DressListView(ListCreateAPIView):
    serializer_class = DressSerializer
    queryset = Dress.objects.all()


__all__ = ['DressListView']