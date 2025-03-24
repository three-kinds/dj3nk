# -*- coding: utf-8 -*-
from django.db import models
from .natural_key_generator import NaturalKeyGenerator


nkg = NaturalKeyGenerator()


def gnk() -> int:
    return nkg.generate_nk()


class NKModel(models.Model):
    id = models.BigIntegerField('id', primary_key=True, default=gnk)

    class Meta:
        abstract = True
