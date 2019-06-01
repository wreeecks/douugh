This is a simple API built using Django Rest Framework. 

## Requirements 

* Python version 3.6.x
* virtualenv
* pip
* django
* django rest framwork (DRF)


## Setup & Running the app

1. Clone repository using GIT
```
> git clone git@github.com:wreeecks/douugh.git
```

2. Change directory to src 
```
> cd douugh
```

3. Create and activate virtual environment
```
> virtualenv env
> source env/bin/activate
```

3. Install Django and DRF
```
> pip install -r requirements.txt
```

4. Make initial migration then run migrate
```
> python manage.py makemigrations
> python manage.py migrate
```

5. (Optional) Create a Django superuser
```
> python manage.py createsuperuser
```


6. Run server
```
> python manage.py runserver

#output
Django version 2.2.1, using settings 'codetest.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Creating a user using DRF browsable api
1. Open http://127.0.0.1/api/create on any browser
2. Fill up the form, then click "Post" button.

## Logging-in using DRF browsble api
1. Open http://127.0.0.1/api/login on any browser
2. Fill up the form, then click "Post" button. This should return a 32 bit string token.


## Testing

1. Change dir to the application root directory 
```
> cd douughcodetest
```

2. Activate virtual env
```
> source env/bin/activate
```

3. Run test
```
> python manage.py test
