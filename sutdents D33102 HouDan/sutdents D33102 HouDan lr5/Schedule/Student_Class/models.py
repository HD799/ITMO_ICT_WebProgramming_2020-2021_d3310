from django.db import models


class Class(models.Model):
    group_number = models.CharField(max_length=10, null=True, blank=True)

class Student(models.Model):
    gerser_list = ((0, "male"), (1, "female"))
    genser = models.BooleanField(default=0, choices=gerser_list)
    name = models.CharField(max_length=40)
    id_group = models.ForeignKey(Class, null=True, blank=True, on_delete=models.SET_NULL)

class Discipline(models.Model):
    subject = models.CharField(max_length=60)

class Teacher(models.Model):
    name = models.CharField(max_length=40)

class Schedule(models.Model):
    date = models.DateTimeField()
    id_group = models.ForeignKey(Class, null=True, blank=True, on_delete=models.SET_NULL)
    id_teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL)
    id_discipline = models.ForeignKey(Discipline, null=True, blank=True, on_delete=models.SET_NULL)

class homworke(models.Model):
    contents_homework=models.CharField(max_length=100)
    release_time = models.DateTimeField()
    Complete_time = models.DateTimeField(null=True,blank=True)
    carry=((0,"not done"), (1,"finished"))
    carry_out = models.BooleanField(choices=carry)
    id_student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    id_teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL)
    id_discipline = models.ForeignKey(Discipline, null=True, blank=True, on_delete=models.SET_NULL)



