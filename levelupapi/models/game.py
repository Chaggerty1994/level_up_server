from operator import mod
from django.db import models
from django.contrib.auth.models import User
from levelupapi.models.game_type import Game_Type
from levelupapi.models.gamer import Gamer

class Game(models.Model):

    game_type = models.ForeignKey(Game_Type, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()