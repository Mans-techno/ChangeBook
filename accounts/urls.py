from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_view, logout_view, profile_view


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
