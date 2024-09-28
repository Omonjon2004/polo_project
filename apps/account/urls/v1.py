from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.account.api_endpoints import auth, activation, user_card
from apps.account.api_endpoints.auth import ProfileViewSet, ChangePasswordViewSet

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'', ChangePasswordViewSet, basename='change-password')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', auth.LoginView.as_view() ),
    path('register/', auth.RegisterView.as_view() ),
    path('forgot_password/', auth.ForgotPasswordView.as_view() ),
    path('send-code/', activation.SendActivationCodeView.as_view()),
    path('verify-code/', activation.VerificationCodeView.as_view()),
    path('add-card/', user_card.AddCardView.as_view()),
]