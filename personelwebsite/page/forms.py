from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Bootstrap form-control sınıfı
            'placeholder': 'İsminizi Girin'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Email Adresinizi Girin'
        })
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Telefon Numaranızı Girin',
            'required': False
        })
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Konu Başlığı'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'Mesajınızı Girin',
            'style': 'height: 200px;'
        })
    )
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
