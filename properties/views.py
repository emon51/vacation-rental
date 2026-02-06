from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Property, Location


def home(request):
    return render(request, 'properties/home.html')


def search(request):
    location_query = request.GET.get('location', '')
    properties = Property.objects.all().select_related('location').prefetch_related('images')
    
    if location_query:
        properties = properties.filter(
            location__city__icontains=location_query
        ) | properties.filter(
            location__state__icontains=location_query
        ) | properties.filter(
            location__country__icontains=location_query
        )
    
    paginator = Paginator(properties, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'location_query': location_query,
    }
    return render(request, 'properties/search.html', context)


def property_detail(request, pk):
    property_obj = get_object_or_404(Property.objects.select_related('location').prefetch_related('images'),pk=pk)
    context = {
        'property': property_obj,
    }
    return render(request, 'properties/property_detail.html', context)