from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from .forms import studentForm, classForm ,hwForm
from .models import Student, Class,homworke

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

def delete_homworke_deta(respons,pk):
    d = homworke.objects.get(pk=pk)
    d.delete()
    return HttpResponse("Deletede")

def create_hw(request):
    context = {}
    form = hwForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_hw.html", context)

class hwUpdateView(UpdateView):
  model = homworke
  fields = ['contents_homework','release_time','Complete_time','carry_out','id_student','id_teacher','id_discipline']
  success_url = "/class_list/"
  template_name = 'update_hw.html'

def base(response):
    return render(response, "base3.html")
