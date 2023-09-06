from django.shortcuts import render
from django.http import HttpResponse
import logging
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)


# def index(request):
#     html = '<h1>Это мой первый сайт</h1>' \
#            '<p>Он довольно неказистый</p>'
#     logger.info('Пользователь посетил главную страницу')
#     return HttpResponse(html)
#
#
# def about(request):
#     html = '<h1>Это информация обо мне</h1>' \
#            '<p>Но я немногословен</p>'
#     logger.info('Пользователь посетил страницу "О нас"')
#     return HttpResponse(html)

def index(request):
    context = {'title': 'Домашняя страница'}
    return render(request, 'my_app/home.html', context)


class About(TemplateView):
    template_name = 'my_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'Обо мне'
        return context


# def about(request):
#     return render(request, 'my_app/about.html')
