# MySentry

# Overview
     for server
        Python 3.6.8
    
        Django 2.1
    
        django-crispy-forms = "==1.7.2"
        
        requests 
    
        pytest 
        
        twine
        
     for client
        Python 3.6.8
        
        MySentry-pkg-Artem2k 0.0.3
        
        requests
        

# Install
    for server
        $ git clone https://github.com/Artem2K/MySentry/
        
    for client
        $ git clone https://github.com/Artem2K/related-programs-to-MySelery

# Usage
    for server
        $ cd MySentry
    
        $ pipenv install
    
        $ pipenv shell
    
        $ python manage.py makemigrations
    
        $ python manage.py migrate
    
        $ python manage.py runserver
    
        open the website and input
        http://127.0.0.1:8000/
        
        $ python manage.py test
        
        
    for client
        $ pipenv install
    
        $ pipenv shell
        
        $ python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps MySentry-pkg-Artem2k==0.0.3 

        $ https://github.com/Artem2K/related-programs-to-MySelery/blob/master/test_error_scripts/README.md 
# URLS
    http://127.0.0.1:8000/ - homepage

    http://127.0.0.1:8000/signup/ - registration

    http://127.0.0.1:8000/users/login/ - login

    http://127.0.0.1:8000/error_list/ - list of all errors in the database, sorting by type is possible

    http://127.0.0.1:8000/apps/ - list of all applications registered on you

    http://127.0.0.1:8000/apps/# - error statistics for the current application, more detailed information,
    sorting by date and type

    