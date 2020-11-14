from django.shortcuts import render
from .models import student

def get_students(request):
    context = {}
    context["dataset"] = student.objects.all()
    return render(request, "students.html", context)

from django.views.generic.list import ListView
class studentlist(ListView):
    model = student
    template_name ='students_list.html'

from django.views.generic.detail import DetailView
class studentDetas (DetailView):
    model = student
    template_name = "studentsDetas.html"


