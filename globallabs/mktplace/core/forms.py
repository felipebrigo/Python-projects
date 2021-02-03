from django import forms
from .models import Product, Contract


class ProductForm(forms.ModelForm):
    class Meta:
        # FIELDS WHICH WILL BE INTO FORM CREATED
        model = Product
        fields = ['code', 'element', 'alloy', 'shape', 'stock', 'price']


class ContractForm(forms.ModelForm):
    class Meta:
        # FIELDS WHICH WILL NOT BE INTO FORM CREATED
        model = Contract
        fields = [
            'contractNumber',
            'isPurchase',
            'counterParty',
            'product',
            'alloy',
            'shape',
            'isRange',
            'minVol',
            'maxVol',
            'originSupplier',
            'allocationCtr'
            ]

