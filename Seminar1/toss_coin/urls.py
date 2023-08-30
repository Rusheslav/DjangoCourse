from django.urls import path
from . import views

urlpatterns = [
    path('coin', views.head_tails, name='coin'),
    path('dice', views.dice, name='dice'),
    path('randomize', views.randomize, name='randomize'),
]
