# Generated by Django 3.1.1 on 2020-11-24 05:32

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(max_length=30)),
                ('Colour', models.CharField(max_length=30)),
                ('state_number', models.CharField(db_column='state number', max_length=3)),
                ('Car_type', models.CharField(choices=[('A', 'Motorcycle'), ('B', 'car'), ('C', 'truck'), ('D', 'bus')], db_column='Car type', max_length=1)),
            ],
            options={
                'db_table': 'Car',
            },
        ),
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first name', max_length=30)),
                ('last_name', models.CharField(db_column='last name', max_length=30)),
                ('birthday', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'driver',
            },
        ),
        migrations.CreateModel(
            name='UserDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('passport', models.PositiveIntegerField()),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ownership_day', models.DateTimeField()),
                ('OW_Car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OneApp.car')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OneApp.driver')),
            ],
            options={
                'db_table': 'Ownership',
            },
        ),
        migrations.CreateModel(
            name='driver_license',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=10)),
                ('Date_issue', models.DateTimeField()),
                ('driver_type', models.CharField(choices=[('A', 'Motorcycle'), ('B', 'car'), ('C', 'truck'), ('D', 'bus')], max_length=1)),
                ('driver_license_driver', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OneApp.driver')),
            ],
            options={
                'db_table': 'driver license',
            },
        ),
        migrations.AddField(
            model_name='driver',
            name='Driver_self',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]