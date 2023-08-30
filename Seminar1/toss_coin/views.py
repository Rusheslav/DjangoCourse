from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging


logger = logging.getLogger(__name__)


def head_tails(request):
    result = 'Head' if randint(0, 1) else 'Tails'
    logger.info(result)
    return HttpResponse(result)


def dice(request):
    result = randint(1, 6)
    logger.info(result)
    return HttpResponse(result)


def randomize(request):
    result = randint(0, 100)
    logger.info(result)
    return HttpResponse(result)
