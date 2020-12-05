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
from django.urls import path, include
from Student_Class import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('D-S/', include("Discipline_schedule.urls")),
    path('student_list/', views.student_list.as_view()),
    path('student_date/<int:pk>/', views.student_deta.as_view()),
    path('student_create/', views.create_student),
    path('class_create/', views.create_class),
    path('student_delete/<int:pk>/', views.delete_student_deta),
    path('student_update/<int:pk>/', views.studentUpdateView.as_view()),
    path('class_list/', views.class_list.as_view()),
    path('class_date/<int:pk>/', views.class_deta.as_view()),
]

