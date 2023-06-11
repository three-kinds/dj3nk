from django.db import models
from dj3nk import NKModel


class User(NKModel):
    username = models.CharField(max_length=32)
