from django.urls import path
from . import views

urlpatterns = [
    path('coin/<int:count>', views.HeadTails.as_view(), name='coin'),
    path('dice/<int:count>', views.Dice.as_view(), name='dice'),
    path('randomize/<int:count>', views.Randomize.as_view(), name='randomize'),
    path('last_games', views.last_games, name='last_games'),
    path('choose_game', views.ChooseGame.as_view(), name='choose_game'),
]
