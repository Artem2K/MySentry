# MySentry

# Overview

    Python 3.6.8
    
    Django 2.1
    
    django-crispy-forms = "==1.7.2"
        
    requests 
    
    pytest 
        
    twine
        

# Install
    
    $ git clone https://github.com/Artem2K/MySentry/

# Usage

    $ cd MySentry
    
    $ pipenv install
    
    $ pipenv shell
    
    $ python manage.py makemigrations
    
    $ python manage.py migrate
    
    $ python manage.py runserver
    
    $ open the website and input: http://127.0.0.1:8000/
        
    $ python manage.py test
        
# URLS
    http://127.0.0.1:8000/ - homepage

    http://127.0.0.1:8000/signup/ - registration

    http://127.0.0.1:8000/users/login/ - login

    http://127.0.0.1:8000/error_list/ - list of all errors in the database, sorting by type is possible

    http://127.0.0.1:8000/apps/ - list of all applications registered on you

    http://127.0.0.1:8000/apps/# - error statistics for the current application, more detailed information,
    sorting by date and type

    