# Generated by Django 3.1.1 on 2020-11-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Class', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='group_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
