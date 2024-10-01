from django.urls import path
from django.urls import path
from apps.product.api_endpoints import shoes, dress

urlpatterns = [
    path('shoes/', shoes.ShoesListView.as_view(), name='shoes'),
    path('shoes/<int:pk>/', shoes.ShoesDetailView.as_view(), name='shoes-detail'),
    path('dress/',dress.DressListView.as_view(), name='dress'),

]

