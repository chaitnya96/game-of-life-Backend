# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class StoreApi(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()
    box = models.BooleanField(default=False)

    def __str__(self):
        return str(self.row)