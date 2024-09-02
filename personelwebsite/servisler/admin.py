from django.contrib import admin
from . models import Service

admin.site.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']
    search_fields = ['title', 'description']
    list_filter = ['title']
    class Meta:
        model = Service
# Register your models here.
