from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from Student_Class.models import Class,Schedule,Discipline,Teacher
from  .forms import TeacherForm, ScheduleForm

# class schedule_list(ListView):
#     model = Schedule
#     template_name = "schedule_list.html"

# class teacher_list(ListView):
#     model = Teacher
#     template_name = "teacher_list.html"

def create_teacher(request):
    context = {}
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_teacher.html", context)

def teacher_list(response):
    Ts = Teacher.objects.all()
    mathematics = Ts.filter(name__contains="math")
    informationToechnolgy = Ts.filter(name__contains="Information")
    physical = Ts.filter(name__contains="Physics")
    English = Ts.filter(name__contains="English")
    physicaleducation = Ts.filter(name__contains="P.E.")
    contex = locals()
    return render(response, "teacher_list.html", context=contex)


class scheduleUpdateView(UpdateView):
  model = Schedule
  fields = ["date", "id_group", "id_teacher", "id_discipline"]
  success_url = "/student_list"
  template_name = 'update_schedule.html'


def create_schedule(request):
    context = {}
    form = ScheduleForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_schedule.html", context)

def schedule_list(response,idgroup):
    Schdules = Schedule.objects.filter(id_group=idgroup)
    Monday = Schdules.filter(date__week_day=1)
    Tuesday = Schdules.filter(date__week_day=2)
    Wednesday = Schdules.filter(date__week_day=3)
    Thursday = Schdules.filter(date__week_day=4)
    Friday= Schdules.filter(date__week_day=5)
    Saturday = Schdules.filter(date__week_day=6)
    Sunday = Schdules.filter(date__week_day=0)
    return render(response, "schedule_list.html" , context=locals())