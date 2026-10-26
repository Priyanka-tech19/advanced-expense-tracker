from django.forms import ModelForm
from .models import Expense
from django import forms

class ExpenseForm(ModelForm):
    class Meta:
        model=Expense
        #fields=('name','amount','category')
        fields='__all__'
        
