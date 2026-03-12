from django.contrib import admin
from django.urls import path
from.views import *

urlpatterns = [
    path('game', game_page, name='game_page'),
    path('', register, name='register'),
    path('signin',signin, name='login'),
    path('game_history', gamehistory, name='gamehistory'),
    path('tournament', tournament_list, name='tournament'),
    path('tour_history',tournament_history, name='tournament_history'),
    path('main',main, name='main'),
    path('nav', nav, name='nav'),
    path('win', win, name='win' )
]