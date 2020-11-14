from django.urls import path
from TwoApp import views


urlpatterns = [
    path("getstudents/", views.get_students),
    path("get_student_list/", views.studentlist.as_view()), #使用.as_view来使用ListView给模板中提供list
    path("deta/<int:pk>/", views.studentDetas.as_view()),
]