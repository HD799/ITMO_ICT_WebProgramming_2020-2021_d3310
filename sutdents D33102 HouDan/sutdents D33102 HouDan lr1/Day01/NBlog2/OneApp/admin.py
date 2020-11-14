from django.contrib import admin
from .models import driver, driver_license, Car, Ownership

admin.site.register(driver)
admin.site.register(driver_license)
admin.site.register(Car)
admin.site.register(Ownership)
