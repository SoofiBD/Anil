from django.shortcuts import render
from django.views.generic import FormView
from . forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

class ContactView(SuccessMessageMixin,FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'Mesajınız başarıyla gönderildi.'
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    