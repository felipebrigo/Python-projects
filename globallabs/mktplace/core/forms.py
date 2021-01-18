from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # FIELDS WHICH WILL BE INTO FORM CREATED
        fields = ['code', 'element', 'alloy', 'shape', 'stock', 'price']


        # FIELDS WHICH WILL NOT BE INTO FORM CREATED

