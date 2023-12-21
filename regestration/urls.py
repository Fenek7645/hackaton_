from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import UserPasswordChangeView



# Здесть мы отслеживаем url адреса по которым переходит пользователь
urlpatterns = [
    path('', views.regestration, name="reg_home"),
    path('enterens/', views.enterens, name="enterens"),
    path('profile/', views.profile, name="profile"),
    path('logout/', auth_views.LogoutView.as_view(), name= "logout"),
     path('profile/password_change', UserPasswordChangeView.as_view(), name='password_change'),
]