from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from .forms import studentForm, classForm
from .models import Student, Class

from .models import Student

class student_list(ListView):
    model = Student
    template_name = "student_list.html"

def create_student(request):
    context = {}
    form = studentForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_student.html", context)

def create_class(request):
    context = {}
    form = classForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_class.html", context)

class student_deta(DetailView):
    model = Student
    template_name = "student_date.html"

def delete_student_deta(respons,pk):
    d = Student.objects.get(pk=pk)
    d.delete()
    return render(respons, 'delete_student_deta.html')

class studentUpdateView(UpdateView):
  model = Student
  fields = ['name', 'id_group', 'genser']
  success_url = "/student_list/"
  template_name = 'update_student.html'

class class_list(ListView):
    model = Class
    template_name = "class_list.html"

class class_deta(DetailView):
    model = Class
    template_name = "class_date.html"
