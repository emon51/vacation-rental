from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q
from django.conf import settings
from .models import Property, Location


def home(request):
    return render(request, 'properties/home.html')


def property_list(request):
    location_query = request.GET.get('location', '').strip()
    properties = Property.objects.all().select_related('location').prefetch_related('images')
    
    if location_query:
        # Try to match the full query first (for autocomplete selections)
        full_match = properties.filter(
            Q(location__city__iexact=location_query) |
            Q(location__state__iexact=location_query) |
            Q(location__country__iexact=location_query)
        )
        
        if full_match.exists():
            properties = full_match
        else:
            # Split and use AND logic for multiple parts
            query_parts = [part.strip() for part in location_query.split(',') if part.strip()]
            
            for part in query_parts:
                properties = properties.filter(
                    Q(location__city__icontains=part) |
                    Q(location__state__icontains=part) |
                    Q(location__country__icontains=part) |
                    Q(location__name__icontains=part)
                )
    
    properties = properties.distinct()
    paginator = Paginator(properties, settings.PROPERTIES_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'location_query': location_query,
    }
    return render(request, 'properties/property_list.html', context)


def property_detail(request, pk):
    property_obj = get_object_or_404(
        Property.objects.select_related('location').prefetch_related('images'),
        pk=pk
    )
    context = {
        'property': property_obj,
    }
    return render(request, 'properties/property_detail.html', context)


def location_autocomplete(request):
    query = request.GET.get('q', '').strip()
    
    if len(query) < 2:
        return JsonResponse({'locations': []})
    
    locations = Location.objects.filter(
        Q(city__icontains=query) |
        Q(state__icontains=query) |
        Q(country__icontains=query) |
        Q(name__icontains=query)
    ).distinct()[:10]
    
    results = []
    for location in locations:
        results.append({
            'id': location.id,
            'text': str(location),
            'city': location.city,
            'state': location.state,
            'country': location.country
        })
    
    return JsonResponse({'locations': results})