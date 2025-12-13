from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title= models.CharField(max_length=200)
    completed=models.BigIntegerField(default=False)
    
from django.db import models

class Party(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.CharField(max_length=200)   # e.g. "logos/anc.png"
    leader = models.CharField(max_length=200) # e.g. "leaders/ramaphosa.png"

    def __str__(self):
        return self.name

class Vote(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
