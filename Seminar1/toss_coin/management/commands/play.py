from random import randint

from django.core.management import BaseCommand

from toss_coin.models import GameModel


class Command(BaseCommand):
    help = 'Toss a coin (Head or Tails)'

    def handle(self, *args, **kwargs):
        result = ('HEAD', 'TAILS')[randint(0, 1)]
        game = GameModel(result=result)
        game.save()

        self.stdout.write(f'{result}')
