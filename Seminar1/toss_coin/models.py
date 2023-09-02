from django.db import models
from django.db.models import Manager


class GameModel(models.Model):
    result = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    objects = Manager()

    def __str__(self):
        return f'<p>Результат игры: {self.result}, время: {self.date}</p>'

    class Meta:
        ordering = ['-date']

    @staticmethod
    def return_last(n):
        return GameModel.objects.all()[:n]
