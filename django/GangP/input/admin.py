from django.contrib import admin
from .models import SoftwareSpec, ChoosenSpec
# Register your models here.

admin.site.register(SoftwareSpec)
admin.site.register(ChoosenSpec)