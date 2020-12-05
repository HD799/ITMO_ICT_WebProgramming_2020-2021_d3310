from django import forms
from .models import Student, Class


class studentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'id_group', 'genser']


class classForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['group_number']
