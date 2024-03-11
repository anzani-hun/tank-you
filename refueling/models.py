from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Refuel(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    created = models.DateTimeField(auto_now_add = True)

    distance = models.PositiveIntegerField()

    petrol_amount_litre = models.PositiveIntegerField()

    refuel_date = models.DateTimeField()

    