from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.ServiceListView.as_view(), name='service-list'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    #path('services/create/', views.ServiceCreateView.as_view(), name='service-create'),
    #path('services/<int:pk>/update/', views.ServiceUpdateView.as_view(), name='service-update'),
    #path('services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service-delete'),
]