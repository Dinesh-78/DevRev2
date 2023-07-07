from django.db import models

import datetime
# Create your models here.
from django.utils import timezone



class VaccineCenters(models.Model):
    class Dosechoice(models.TextChoices):
        DOSE1: '1'
        DOSE2: '2'
        DOSE3: '3'

    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    otime = models.TimeField(default=timezone.now())
    ctime = models.TimeField(default=timezone.now())
   # selecton = models.CharField(max_length=1, choices=Dosechoice.choices)


class dosage(models.Model):
    dname = models.CharField(max_length=300)


class User(models.Model):
    name = models.CharField(max_length=200)
