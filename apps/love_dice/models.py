from django.db import models


class Memo(models.Model):
    problem = models.CharField(max_length=1000)
    winner = models.CharField(max_length=10)
    policy = models.TextField(max_length=1000)
