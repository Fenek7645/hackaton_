from django.urls import path
from . import views

# Здесть мы отслеживаем url адреса по которым переходит пользователь
urlpatterns = [
    path('', views.courses, name="main_courses"),
    path('personal_data/', views.personal_data, name="personal_data"),
    path('personal_data/suppourt', views.helpa, name="helpa"),
    path('personal_data/data_rules', views.rule_data, name="rule_data"),
    path('personal_data/web_rules', views.rule_web, name="rule_web"),
    path('personal_data/web_rules/password', views.password, name="password"),
    path('personal_data/social_network', views.rule_social_network, name="rule_social_network"),
    path('theory/', views.theory, name="theory"),
    path('scammers/', views.mosheniki, name="mosheniki_main"),
    path('scammers/viruses', views.mosheniki_viruses, name="mosheniki_viruses"),
    path('scammers/phishing', views.mosheniki_fishing, name="mosheniki_fishing"),
    path('scammers/financial_pyramid', views.mosheniki_fin_piromida, name="mosheniki_fin_piromida"),
    path('scammers/coshial_ingeering', views.mosheniki_coshial_ingeering, name="mosheniki_coshial_ingeering"),
]   