from django.db import models

# Create your models here.


class Product(models.Model):
    code = models.CharField(max_length=10, null=False, blank=False)
    element = models.CharField(max_length=20, null=False, blank=False)
    alloy = models.CharField(max_length=10, null=False, blank=False)
    shape = models.CharField(max_length=20, null=False, blank=False)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.code


class Contract(models.Model):
    contractNumber = models.CharField(max_length=16, null=False, blank=False)
    counterParty = models.CharField(max_length=100, null=False, blank=False)
    contractCounterParty = models.CharField(max_length=50)
    product = models.CharField(max_length=50, null=False, blank=False)
    alloy = models.TextField()
    minVol = models.IntegerField()
    maxVol = models.IntegerField()
    lastChangeUser = models.TextField()

    def __str__(self):
        return self.contractNumber




