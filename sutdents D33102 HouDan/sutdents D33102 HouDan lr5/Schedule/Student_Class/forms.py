from django import forms
from .models import Student, Class,homworke


class studentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'id_group', 'genser']


class classForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['group_number']

class hwForm(forms.ModelForm):
    class Meta:
        model = homworke
        fields = ['contents_homework','release_time','Complete_time','carry_out','id_student','id_teacher','id_discipline']
