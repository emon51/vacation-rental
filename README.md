# Vacation Rental Property Management System

A Django-based web application for managing and browsing vacation rental properties with advanced search functionality and image management.

## Features

- **Property Management**: Add, edit and manage vacation rental properties from admin panel.
- **Location-based Organization**: Properties organized by location (City, State, Country)
- **Image Gallery**: Multiple images per property with carousel navigation
- **Search Functionality**: Search properties by location with autocomplete
- **Pagination**: Browse properties with paginated results
- **Admin Dashboard**: Full-featured admin panel with filters and inline image uploads
- **CSV Import**: Bulk import properties from CSV files

## Technologies Used

- **Backend**: Django
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript
- **Image Handling**: Pillow

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
```bash
   git clone https://github.com/emon51/vacation-rental.git
```
2. **Change directory**
```bash
   cd vacation-rental
```

3. **Create virtual environment**
```bash
   python3 -m venv venv
```
4. **Activate vurtual environment**

On Linux
```bash
   source venv/bin/activate
```
On Windows
```bash
   venv\Scripts\activate
```


5. **Install dependencies**
```bash
pip install -r requirements.txt
```

6. **Run migrations**
```bash
   python manage.py makemigrations
   python manage.py migrate
```

7. **Create superuser**
```bash
   python manage.py createsuperuser
```

8. **Import sample data**
```bash
   python manage.py import_csv properties_data.csv
```

9. **Run development server**
```bash
   python manage.py runserver
```

10. **Access the application**
   - Homepage: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/
   - Properties List: http://127.0.0.1:8000/property-list/

## Project Structure
```
rental/
├── vacation_rental/               # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── properties/                    # Main application
│   ├── models.py                  # Database models
│   ├── views.py                   # View logic
│   ├── admin.py                   # Admin configuration
│   ├── urls.py                    # URL routing
│   └── management/
│       └── commands/
│           └── import_csv.py      # CSV import command
├── templates/
│   └── properties/
│       ├── base.html              # Base template
│       ├── home.html              # Homepage
│       ├── property_list.html     # Property listing
│       ├── property_detail.html   # Property details
│       └── search_bar.html        # Reusable search component
├── media/                         # Uploaded images
│   └── property_images/
├── properties_data.csv            # Sample data (Generated using AI)
├── manage.py
└── README.md
```

## Database Models

### Location
- `name`: Location display name
- `country`: Country name
- `state`: State/Province name (optional)
- `city`: City name

### Property
- `location`: Foreign key to Location
- `title`: Property title
- `description`: Detailed description
- `price_per_night`: Nightly rental price
- `bedrooms`: Number of bedrooms
- `bathrooms`: Number of bathrooms
- `max_guests`: Maximum guest capacity

### Image
- `property`: Foreign key to Property
- `image`: Image file (stored in media/property_images/)
- `is_primary`: Mark as primary/featured image

## Usage

### Adding Properties

1. Login to admin panel at `/admin/`
2. Navigate to "Properties"
3. Click "Add Property"
4. Fill in property details
5. Add images using the inline image form
6. Save the property

### Uploading Images

- Images can be uploaded through the admin panel
- Multiple images per property supported
- Images stored in `media/property_images/`
- First image is displayed as primary in listings
- All images shown in carousel on detail page

### Importing from CSV

CSV file format:
```csv
location_name,country,state,city,title,description,price_per_night,bedrooms,bathrooms,max_guests
Destin Florida,USA,Florida,Destin,Beach House,Description,350.00,4,3,8
```

Import command:
```bash
python manage.py import_csv properties_data.csv
```

### Search Functionality

- **Autocomplete**: Start typing city, state, or country
- **Flexible Search**: Matches partial text across all location fields
- **Pagination**: 6 properties per page (configurable in settings)

## Configuration

### Pagination Settings

Edit `vacation_rental/settings.py`:
```python
PROPERTIES_PER_PAGE = 6  # Change to desired number
```

### Media Files

Media files are stored in:
- Development: `media/` directory in project root
- Production: Configure `MEDIA_ROOT` and `MEDIA_URL` accordingly

## API Endpoints

- `/` - Homepage with search
- `/property-list/` - Property listing with search and pagination
- `/property/<id>/` - Property detail page
- `/api/locations/?q=<query>` - Location autocomplete API
- `/admin/` - Admin dashboard

## Development

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Features in Detail

### Image Carousel
- Left/right navigation buttons
- Keyboard support (arrow keys)
- Image counter (e.g., "1 / 5")
- Buttons hidden at first/last images
- Smooth transitions

### Search Features
- Real-time autocomplete
- Debounced API calls (300ms)
- Supports city, state, country searches
- AND logic for multiple search terms
- Case-insensitive matching

### Admin Features
- Inline image upload
- List filters by location, bedrooms, bathrooms
- Search functionality
- Bulk actions support


## License

This project is created for educational purposes