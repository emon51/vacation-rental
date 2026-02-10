from django.contrib import admin
from .models import Location, Property, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'state', 'country']
    list_filter = ['country', 'state']
    search_fields = ['city', 'state', 'country', 'name']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'price_per_night', 'bedrooms', 'bathrooms', 'max_guests']
    list_filter = ['location__country', 'location__city', 'bedrooms', 'bathrooms']
    search_fields = ['title', 'description', 'location__city']
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['property', 'image', 'is_primary']
    list_filter = ['is_primary']