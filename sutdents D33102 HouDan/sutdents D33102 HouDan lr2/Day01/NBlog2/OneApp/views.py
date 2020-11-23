from django.http import Http404
from django.shortcuts import render
from .models import driver,Car,Ownership
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import driverForm

def detail(request, driver_id):
    try:
        dr = driver.objects.get(pk=driver_id)
    except driver.DoesNotExist:
        raise Http404("driver does not exist")  #用django raise抛出异常
    return render(request, 'driver.html', {'driver': dr})

class driver_list(ListView):
    model = Ownership
    template_name = "driver_list.html"
class drivers(ListView):
    model = driver
    template_name = "drivers.html"

class driver_deta(DetailView):
    model = driver
    template_name = "driver_date.html"

class Car_deta(DetailView):
    model = Car
    template_name = "Car_deta.html"

def delete_driver_deta(respons,pk):
    d = driver.objects.get(pk=pk)
    d.delete()
    return render(respons, 'delete_driver_deta.html')


def create_view(request):
    context = {}
    form = driverForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)

from django.views.generic.edit import UpdateView

class driverUpdateView(UpdateView):
  model = driver
  fields = ['first_name', 'last_name', 'birthday']
  success_url = '/driver_list/'
  template_name = 'update_driver.html'

