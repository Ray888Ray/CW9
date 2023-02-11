from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView, UserDetailView, UserChangeView, UserPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('change/', UserChangeView.as_view(), name='user_change'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change')
]