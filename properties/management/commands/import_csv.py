import csv
from django.core.management.base import BaseCommand
from properties.models import Location, Property


class Command(BaseCommand):
    help = 'Import properties from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Get or create location
                location, created = Location.objects.get_or_create(
                    city=row['city'],
                    country=row['country'],
                    defaults={
                        'name': row['location_name'],
                        'state': row['state'],
                    }
                )
                
                # Create property
                property_obj = Property.objects.create(
                    location=location,
                    title=row['title'],
                    description=row['description'],
                    price_per_night=row['price_per_night'],
                    bedrooms=row['bedrooms'],
                    bathrooms=row['bathrooms'],
                    max_guests=row['max_guests']
                )
                
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully imported: {property_obj.title}')
                )
        
        self.stdout.write(self.style.SUCCESS('CSV import completed! Images can be uploaded via admin panel.'))