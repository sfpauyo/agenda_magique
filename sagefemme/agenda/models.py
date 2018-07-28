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
    perinee_status=1
    grossesse_status=2
    gynneco_status=3
    diu_status=4
    nexplanon_status=5
    retrait_status=6
    epp_status=7
    epnp_status=8
    cours_status=9
    TYPE_STATUS=(
        (perinee_status, "Périnée"),
        (grossesse_status, "Grossesse"),
        (gynneco_status, "Gynéco"),
        (diu_status, "DIU"),
        (nexplanon_status, "Nexplanon"),
        (retrait_status, "Retrait d'implant"),
        (epp_status, "EPP"),
        (epnp_status, "EPNP"),
        (cours_status, "Cours")
        )
    #TODO  delete only future Appointment when Patient is deleted
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField('date de rendez-vous')
    type = models.IntegerField(choices=TYPE_STATUS, default=perinee_status)

    def __str__(self):
        return str(self.date).split(" ")[0] + " " + self.patient.last_name +" "+ self.type
