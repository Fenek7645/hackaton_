from django.urls import path
from . import views


urlpatterns = [
    path('', views.game, name="game_home"),
    path('question_1', views.game1, name="game1"),
    path('question_1_1',views.game1_1, name="game1_1"),
    path('question_1_2',views.game1_2, name="game1_2"),
    path('question_1_3',views.game1_3, name="game1_3"),
    
    path('question_2', views.game2, name="game2"),
    path('question_2_1', views.game2_1, name="game2_1"),
    path('question_2_2', views.game2_2, name="game2_2"),
    path('question_2_3', views.game2_3, name="game2_3"),
    
    path('question_3', views.game3, name="game3"),
    path('question_3_1', views.game3_1, name="game3_1"),
    path('question_3_2', views.game3_2, name="game3_2"),
    path('question_3_3', views.game3_3, name="game3_3"),

    path('question_4', views.game4, name="game4"),
    path('question_4_1', views.game4_1, name="game4_1"),
    path('question_4_2', views.game4_2, name="game4_2"),
    path('question_4_3', views.game4_3, name="game4_3"),
    
    path('question_5', views.game5, name="game5"),
    path('question_5_1', views.game5_1, name="game5_1"),
    path('question_5_2', views.game5_2, name="game5_2"),
    path('question_5_3', views.game5_3, name="game5_3"),
    
    path('question_6', views.game6, name="game6"),
    path('question_6_1', views.game6_1, name="game6_1"),
    path('question_6_2', views.game6_2, name="game6_2"),
    path('question_6_3', views.game6_3, name="game6_3"),
    
    path('question_7', views.game7, name="game7"),
    path('question_7_1', views.game7_1, name="game7_1"),
    path('question_7_2', views.game7_2, name="game7_2"),
    path('question_7_3', views.game7_3, name="game7_3"),
    
    path('question_8', views.game8, name="game8"),
    path('question_8_1', views.game8_1, name="game8_1"),
    path('question_8_2', views.game8_2, name="game8_2"),
    path('question_8_3', views.game8_3, name="game8_3"),
    
    path('question_9', views.game9, name="game9"),
    path('question_9_1', views.game9_1, name="game9_1"),
    path('question_9_2', views.game9_2, name="game9_2"),
    path('question_9_3', views.game9_3, name="game9_3"),
    
    path('question_10', views.game10, name="game10"),
    path('question_10_1', views.game10_1, name="game10_1"),
    path('question_10_2', views.game10_2, name="game10_2"),
    path('question_10_3', views.game10_3, name="game10_3"),
]