from django import forms
from .models import driver

class driverForm(forms.ModelForm):
    class Meta:
        model = driver
        fields = ('first_name', 'last_name', 'birthday')