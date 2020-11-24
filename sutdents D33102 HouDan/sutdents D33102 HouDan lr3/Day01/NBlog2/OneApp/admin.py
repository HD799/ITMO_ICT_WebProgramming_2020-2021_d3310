from django.contrib import admin
from .models import driver, driver_license, Car, Ownership, UserDriver
from django.contrib.auth.admin import UserAdmin

admin.site.register(driver)
admin.site.register(driver_license)
admin.site.register(Car)
admin.site.register(Ownership)

admin.site.register(UserDriver, UserAdmin)
