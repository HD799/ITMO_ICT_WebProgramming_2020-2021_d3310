"""Schedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Discipline_schedule import views

urlpatterns = [
    path('schedule_list/<int:idgroup>/', views.schedule_list),
    path('create_teacher/', views.create_teacher),
    path('teacher_list/', views.teacher_list),
    path('create_schedule/', views.create_schedule),
    path('update_schedule/<int:pk>', views.scheduleUpdateView.as_view()),
    path('update_schedule_list/<int:idgroup>/', views.update_schedule_list),
    path('delete_schedule/<int:pk>/', views.delete_schedule_deta),

]

