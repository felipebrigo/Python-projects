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
    isPurchase = models.BooleanField(default=False, null=False, blank=False)
    counterParty = models.TextField(null=False, blank=False)
    product = models.CharField(max_length=50, null=False, blank=False)
    alloy = models.TextField()
    shape = models.CharField(max_length=10)
    isRange = models.BooleanField(default=False, null=False, blank=False)
    minVol = models.IntegerField()
    maxVol = models.IntegerField()
    originSupplier = models.TextField(null=False, blank=False)
    allocationCtr = models.CharField(max_length=16, null=False, blank=False)

    def __str__(self):
        return self.contractNumber




