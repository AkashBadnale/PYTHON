Read the article here to understand the code :
https://www.bezkoder.com/django-postgresql-crud-rest-framework/

* <h1>Summary</h1> </br>
`pip install djangorestframework` // if already not installed </br>
`django-admin startproject DjangoRestApisPostgreSQL` </br>
</br>

INSTALLED_APPS = [ </br>
    ... </br>
    # Django REST framework  </br>
    'rest_framework', </br>
] </br>
</br>
`pip install psycopg2`  // if already not installed & this is for postgre sql </br>
</br>
//edit database info </br>
DATABASES = { </br>
    'default': { </br>
        'ENGINE': 'django.db.backends.postgresql', </br>
        'NAME': 'testdb', </br>
        'USER': 'postgres', </br>
        'PASSWORD': '123', </br>
        'HOST': '127.0.0.1', </br>
        'PORT': '5432', </br>
    } </br>
} </br>
</br>
cd DjangoRestApisPostgreSQL </br>
`python manage.py startapp tutorials` </br>
</br>
class TutorialsConfig(AppConfig): </br>
    name = 'tutorials' </br>
</br>
INSTALLED_APPS = [ </br>
    ... </br>
    # Tutorials application  </br>
    'tutorials.apps.TutorialsConfig', </br>
] </br>
</br>
`pip install django-cors-headers`  // if already not installed </br>
</br>
INSTALLED_APPS = [ </br>
    ... </br>
    # CORS </br>
    'corsheaders', </br>
] </br>
</br>
MIDDLEWARE = [ </br>
    ... </br>
    # CORS </br>
    'corsheaders.middleware.CorsMiddleware', </br>
    'django.middleware.common.CommonMiddleware', </br>
] </br>
</br>
CORS_ORIGIN_ALLOW_ALL = False </br>
CORS_ORIGIN_WHITELIST = ( </br>
    'http://localhost:8081', </br>
) </br>
</br>
`python manage.py makemigrations tutorials` </br>
`python manage.py migrate tutorials` </br>
</br>
`python manage.py runserver 8080` </br>

