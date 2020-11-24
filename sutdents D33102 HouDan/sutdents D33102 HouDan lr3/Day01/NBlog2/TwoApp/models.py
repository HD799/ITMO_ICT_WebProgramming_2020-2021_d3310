from django.db import models
class student(models.Model):
    S_name = models.CharField(max_length=30 , null=True)
    S_class = models.IntegerField(default=0, null=True)
    def __str__(self):
        return "{} {}".format(self.S_name,self.S_class)