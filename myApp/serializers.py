from django import forms
from .models import Product
#DataFlair
class ProductCreate(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'