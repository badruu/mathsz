from django import forms
from .models import *

class MathsForm(forms.ModelForm):
    class Meta:
        model = Maths
        exclude = ['instructor','timestamp']

# class BusinessForm(forms.ModelForm):
#     class Meta:
#         model = Business
#         exclude = ['user', 'hood_id']
