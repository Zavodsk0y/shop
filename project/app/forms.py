from django import forms

from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Поиск')