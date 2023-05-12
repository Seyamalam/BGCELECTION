from django.db import models

# Create your models here.
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    votes = models.IntegerField()

class Voter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    voted = models.BooleanField(default=False)