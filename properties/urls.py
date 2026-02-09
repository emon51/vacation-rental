from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    path('', views.home, name='home'),
    path('property-list/', views.property_list, name='property-list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('api/locations/', views.location_autocomplete, name='location_autocomplete'),
]