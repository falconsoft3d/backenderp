from django import forms
from ..models.product import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = PyProduct
        fields = [
            'name',
            'code',
            'carcode',
            'description',
        ]