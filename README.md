# ecommerce_api


## Dependencies
* Python (3.5, 3.6, 3.7, 3.8, 3.9)
* pip3
* Django (2.2, 3.0, 3.1)
* google-api-python-client


## Installation

**API**
```bash
pip install djangorestframework
pip install dj-rest-auth
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
pip install psycopg2 # for working with postgres
```

**App**
```bash
pip install django
django-admin startproject dj_api
python manage.py migrate
```

**Google Authentication**
```bash
pip install --upgrade google-api-python-client
```


## Change API Settings

**Settings**
```python 
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_api',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'StoreDB',
        'USER': 'postgres',
        'PASSWORD': '*************',
        'HOST': 'localhost',
    }
}
```

**URL path**
```python
urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
```

**Install**
```bash
pip install psycopg2-binary  
```