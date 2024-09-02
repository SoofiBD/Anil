from django.shortcuts import render
from django.views.generic import ListView
from .models import Service
from django.views.generic import DetailView

# Create your views here.
class ServiceListView(ListView):
    model = Service
    template_name = 'service.html'
    context_object_name = 'services'
    
class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'

def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    return render(request, 'service_detail.html', {'service': service})
    
