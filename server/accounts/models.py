from django.db import models
from django.contrib.auth.models import AbstractUser

from movies.models import Actor

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    like_actors = models.ManyToManyField(Actor, related_name='like_users')
