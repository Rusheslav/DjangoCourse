from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    html = '<h1>Это мой первый сайт</h1>' \
           '<p>Он довольно неказистый</p>'
    logger.info('Пользователь посетил главную страницу')
    return HttpResponse(html)


def about(request):
    html = '<h1>Это информация обо мне</h1>' \
           '<p>Но я немногословен</p>'
    logger.info('Пользователь посетил страницу "О нас"')
    return HttpResponse(html)
