
from django import forms
from django.core.exceptions import ValidationError
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(min_length=3, required=True)
    image = forms.ImageField(required=False)

    def clean_name(self):
        user_entered_name = self.cleaned_data['name']

        # Check if any products with the given name exist in the database
        if Product.objects.filter(name=user_entered_name).exists():
            raise ValidationError("Name must be unique")

        return user_entered_name
    




'''from typing import Any
from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ProductForm(forms.Form):
    name = forms.CharField(min_length=3, required=True)
    image = forms.ImageField(required=False)
    
    def clean_name(self):
        userentername = self.cleaned_data['name']
        obj=Product.objects.get(name=userentername).exists()

        if (obj):
            raise ValidationError("name must be unique")
        else:
            True 
'''


