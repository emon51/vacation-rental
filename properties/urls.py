from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
]