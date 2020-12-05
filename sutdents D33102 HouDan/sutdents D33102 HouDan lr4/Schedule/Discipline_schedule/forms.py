from django import forms
from Student_Class.models import Teacher, Schedule, Discipline

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name"]
class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ["date", "id_group", "id_teacher", "id_discipline"]

