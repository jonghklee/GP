from django.contrib import admin
from .models import SoftwareSpec, ChoosenSpec, othermatters
# Register your models here.

admin.site.register(SoftwareSpec)
admin.site.register(ChoosenSpec)
admin.site.register(othermatters)