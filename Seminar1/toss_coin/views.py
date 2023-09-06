from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging
from django.views.generic import TemplateView

from toss_coin.models import GameModel

logger = logging.getLogger(__name__)


class HeadTails(TemplateView):
    template_name = 'toss_coin/toss.html'

    def get_context_data(self, **kwargs):
        results = ['Head' if randint(0, 1) else 'Tails' for i in range(int(self.kwargs['count']))]
        logger.info(results)
        game = GameModel(result=results)
        game.save()
        context = super().get_context_data()
        context['title'] = 'Монетка'
        context['results'] = results
        return context


# def head_tails(request):
#     result = 'Head' if randint(0, 1) else 'Tails'
#     logger.info(result)
#     game = GameModel(result=result)
#     game.save()
#     return HttpResponse(result)


class Dice(HeadTails):
    def get_context_data(self, **kwargs):
        results = [randint(1, 6) for i in range(int(self.kwargs['count']))]
        logger.info(results)
        game = GameModel(result=results)
        game.save()
        context = super().get_context_data()
        context['title'] = 'Кости'
        context['results'] = results
        return context


def last_games(request):
    last = GameModel().return_last(5)
    return HttpResponse(last)


# def dice(request):
#     result = randint(1, 6)
#     logger.info(result)
#     return HttpResponse(result)

class Randomize(HeadTails):
    def get_context_data(self, **kwargs):
        results = [randint(0, 100) for i in range(int(self.kwargs['count']))]
        logger.info(results)
        game = GameModel(result=results)
        game.save()
        context = super().get_context_data()
        context['title'] = 'Рандом'
        context['results'] = results
        return context

# def randomize(request):
#     result = randint(0, 100)
#     logger.info(result)
#     return HttpResponse(result)
