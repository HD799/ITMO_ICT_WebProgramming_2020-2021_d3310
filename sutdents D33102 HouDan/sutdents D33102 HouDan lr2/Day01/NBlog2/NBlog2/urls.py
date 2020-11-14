"""NBlog2 URL Configuration

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
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.contrib import admin
from django.urls import path, include
from OneApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('getdriver/<int:driver_id>', views.detail),#使用<int:xxx>来传入数据
    path('driver_list/', views.driver_list.as_view()),
    path('driver_deta/<int:pk>/', views.driver_deta.as_view()),
    path('car_deta/<int:pk>/', views.Car_deta.as_view()),
    path('delete_dirver_deta/<int:pk>/', views.delete_driver_deta),
    path('create_driver/', views.create_view),
    path('update_driver/<int:pk>/', views.driverUpdateView.as_view()),
    path('TwoApp/', include("TwoApp.urls")),
]
