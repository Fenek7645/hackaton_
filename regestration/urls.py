from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



# Здесть мы отслеживаем url адреса по которым переходит пользователь
urlpatterns = [
    path('', views.register, name="reg_home"),
    path('enterens/', views.enterens, name="enterens"),
    path('profile/', views.profile, name="profile"),
    path('logout/', auth_views.LogoutView.as_view(), name= "logout"),
    path('accounts/password/change/',  views.change_password, name='passwordchange'),
]