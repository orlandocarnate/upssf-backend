# Django REST API backend

## Models
Add models to the Admin panel in the `admin.py` file.

# Django-Summernote package
`pip install django-summernote` used for rich text editing in the admin panel.

## Images
* need Pillow module to use the ImageField in the model
* assign a `static/images` folder for the images in `settings.py`
```
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = 'static/images'

```

* In the project's `urls.py` add the following:
```
from django.conf import settings
from django.conf.urls.static import static

...

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Make data from database serialized
* create `serializers.py` 

## Deploying to Ubuntu Server on Raspberry Pi

### Create Virtual environment
mkdir /django-servers
cd /django-servers

Create a venv environment folder:
sudo python3 -m venv venv

Run environment:
source venv/bin/activate

install uWSGI
sudo pip install uwsgi