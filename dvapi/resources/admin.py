from django.contrib import admin

from .models import Drug, Vaccination

admin.site.register([Drug, Vaccination])
