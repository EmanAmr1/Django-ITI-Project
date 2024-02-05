from django import forms
from django.core.exceptions import ValidationError
from .models import Category

class CategoryForm(forms.Form):
    name = forms.CharField(min_length=3, required=True)
    image = forms.ImageField(required=False)

    def clean_name(self):
        user_entered_name = self.cleaned_data['name']

        # Check if any products with the given name exist in the database
        if Category.objects.filter(name=user_entered_name).exists():
            raise ValidationError("Name must be unique")

        return user_entered_name
    
class CategoryMetaForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','image']
        
