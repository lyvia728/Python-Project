from django.db import models

class Identity(models.Model):
    id_number = models.CharField(max_length=13, unique=True)
    full_names = models.CharField(max_length=200)
    surname = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.full_names} {self.surname} ({self.id_number})"
