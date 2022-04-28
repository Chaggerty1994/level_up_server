from cProfile import label
from django.db import models
from django.contrib.auth.models import User


class Game_Type(models.model):

    label = models.CharField(max_length=50)