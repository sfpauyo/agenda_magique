from django.db import models
from django.utils import timezone

class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    #TODO add check for duplicate last_name
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200, blank=True)
    email =models.CharField(max_length=200, blank=True)
    term_date = models.DateField('date de terme', blank=True)
    birth_date = models.DateField("date d'accouchement", blank=True)

    def __str__(self):
        if self.first_name is None:
            return self.last_name
        else :
            return self.first_name + " " + self.last_name

    def has_given_birth(self):
        return birth_date is not None


class Appointment(models.Model):
    #TODO  delete only future Appointment when Patient is deleted
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField('date de rendez-vous')
    type = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.type
