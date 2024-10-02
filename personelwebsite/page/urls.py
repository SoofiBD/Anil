from django.urls import path
from . import views
from page.views import ContactView

urlpatterns = [
    path("", views.index, name="index"),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', views.about, name='about'),
]