from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}" if self.state else f"{self.city}, {self.country}"


class Property(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=300)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    max_guests = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Properties'
    
    def __str__(self):
        return self.title


class Image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    is_primary = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Image for {self.property.title}"