# Presto

## Task
Create a RESTful API which returns restaurant's dishes and their toppings.

## Features

### Dependencies
*Python 3.5+*  
Basic Language of the project.  
*Django + Django Rest Framework*   
Used to create api services.
*PsyCopg2*  
PostgreSQL driver for Python.  
*DjangoRestFramework-Recursive*  
Used to create api serializer for Topping model. This library allows to create recursive fields
for models.

### Tests
Test module contains test cases for all endpoints. It checks both API endpoints status codes and
response schema correctness.  
You can run test using command `python3 manage.py test`.

### Response Schema

GET /restaurants/
```json
[
    {
        "title": "McDonalds",
        "address": "Pushkina kolotushkina",
        "rating": 5
    }
]
```

GET /restaurants/1/item/
```json
[
    {
        "name": "Burger",
        "base_cost": 0.0,
        "toppings": [
            {
                "name": "Salad",
                "cost": 0.0,
                "sub_toppings": [
                    {
                        "name": "Cheese",
                        "cost": 0.0,
                        "sub_toppings": []
                    }
                ]
            }
        ]
    }
]
```
## Django motivation  
Django is "Batteries included" framework. It contains all functionality I need
except creating RESTful API endpoints, which are created using Django Rest Framework.
### DjangoRestFramework-Recursive
In DjangoRestFramework by default I can use DRF-nested serializers to create recursive fields. 
But unfortunately, depth of those fields is limited so I was forced to use DRF-Recursive which solves this problem.

## Quick Start
* Clone repository
* Create database 'presto', with owner admin:admin (You can change DB settings in module settings.py )
* While in project root dir, use command `pip3 install -r requirements.txt`
* Use command `manage.py runserver localhost:8000` to run project server
* (Optionally) You can create superuser via `manage.py createsuperuser` to access admin panel
* (Optionally) Run tests using `manage.py test`