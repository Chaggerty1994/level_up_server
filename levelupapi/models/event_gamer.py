
from operator import mod
from django.db import models
from django.contrib.auth.models import User
from levelupapi.models.event import Event

from levelupapi.models.gamer import Gamer


class Event_Gamer(models.Model):

    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)