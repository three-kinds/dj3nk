from django.db import models
from dj3nk.nk_model import NKModel


class User(NKModel):
    username = models.CharField(max_length=32)
