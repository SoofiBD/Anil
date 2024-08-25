from django.shortcuts import render
from django.views.generic import ListView
from .models import Service

# Create your views here.
class ServiceListView(ListView):
    model = Service
    template_name = 'service.html'
    context_object_name = 'services'