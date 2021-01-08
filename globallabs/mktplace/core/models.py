from django.db import models

# Create your models here.

'''
class Material(models.Model):
    code = models.CharField(max_length=10,
                          null=False,
                          blank= False,
                          )
    element = models.CharField(max_length=20,
                          null=False,
                          blank= False,
                               )
    alloy = models.CharField(max_length=10,
                          null=False,
                          blank= False,
                             )
    objects = models.Manager()

    class Meta:
        db_table = 'material'

    def __str__(self):
        return self.code
        
shape
description
                
'''


class Product(models.Model):
    code = models.CharField(max_length=10, null=False, blank=False)
    element = models.CharField(max_length=20, null=False, blank=False)
    alloy = models.CharField(max_length=10, null=False, blank=False)
    shape = models.CharField(max_length=20, null=False, blank=False)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.code




