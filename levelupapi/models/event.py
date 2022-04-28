from cProfile import label
from django.db import models

from levelupapi.models.gamer import Gamer

class Event(models.Model):
    game = models.IntegerField()
    description = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    prganizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)