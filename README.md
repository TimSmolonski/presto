# Presto

## Task
Create a RESTful API which returns restaurant's dishes and their toppings.

## Features

### Dependencies
*Python 3.5+*  
Basic Language of the project.
*Django + Django Rest Framework*   
Used to create api services.
*PostgreSQL + PsyCopg2*  
PostgreSQL was one of the task requirements. PsyCopg2 is PSQL driver for Python. 
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