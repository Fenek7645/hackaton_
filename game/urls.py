from django.urls import path
from . import views


urlpatterns = [
    path('', views.game, name="game_home"),
    path('question_1', views.game1, name="game1"),
    path('question_1_1',views.game1_1, name="game1_1"),
    path('question_1_2',views.game1_2, name="game1_2"),
    path('question_1_3',views.game1_3, name="game1_3"),
    path('question_2', views.game2, name="game2"),
    path('question_3', views.game3, name="game3"),
    path('question_4', views.game4, name="game4"),
    path('question_5', views.game5, name="game5"),
    path('question_6', views.game6, name="game6"),
    path('question_7', views.game7, name="game7"),
    path('question_8', views.game8, name="game8"),
    path('question_9', views.game9, name="game9"),
    path('question_10', views.game10, name="game10"),
]