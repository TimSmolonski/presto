from rest_framework import test, status

from .models import Dish, Restaurant, Topping

URL = 'http://localhost:8000/'
URL_TOPPINGS = URL + 'toppings/'
URL_DISHES = URL + 'dishes/'
URL_RESTAURANTS_LIST = URL + 'restaurants/'


class PrestoTests(test.APITestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(title='TestRestaurant', address='Pushkina-Kolotushkina', rating=3)
        self.pizza = Dish.objects.create(name='Pizza', base_cost=2.28, restaurant=self.restaurant)
        self.filling = Topping.objects.create(name='Filling', cost=0.0)
        self.cheese = Topping.objects.create(name='Cheese', cost=1.0, parent=self.filling)
        self.pepperoni = Topping.objects.create(name='Pepperoni', cost=2.0)
        self.filling.sub_toppings.add(self.pepperoni)
        self.pizza.toppings.add(self.filling)
        self.restaurant.dishes.add(self.pizza)

        self.data_toppings = [
            {
                'name': 'Filling',
                'cost': 0.0,
                'sub_toppings': [
                    {
                        'name': 'Cheese',
                        'cost': 1.0,
                        'sub_toppings': []
                    },
                    {
                        'name': 'Pepperoni',
                        'cost': 2.0,
                        'sub_toppings': []
                    }
                ]
            },
            {
                'name': 'Cheese',
                'cost': 1.0,
                'sub_toppings': []
            },
            {
                'name': 'Pepperoni',
                'cost': 2.0,
                'sub_toppings': []
            }
        ]

        self.data_dishes = {
                'name': self.pizza.name,
                'base_cost': self.pizza.base_cost,
                'toppings': [
                    {
                        'name': 'Filling',
                        'cost': 0.0,
                        'sub_toppings': [
                            {
                                'name': 'Cheese',
                                'cost': 1.0,
                                'sub_toppings': []
                            },
                            {
                                'name': 'Pepperoni',
                                'cost': 2.0,
                                'sub_toppings': []
                            }
                        ]
                    }
                ]
            }

        self.data_restaurants = {
            'title': self.restaurant.title,
            'address': self.restaurant.address,
            'rating': self.restaurant.rating
        }

    def testToppings(self):
        response = self.client.get(path=URL_TOPPINGS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.data_toppings)

    def testDishes(self):
        response = self.client.get(path=URL_DISHES)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [self.data_dishes])

    def testRestaurantsList(self):
        response = self.client.get(path=URL_RESTAURANTS_LIST)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [self.data_restaurants])

    def testRestaurantItem(self):
        response = self.client.get(path=URL_RESTAURANTS_LIST + str(self.restaurant.id) + '/item/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [self.data_dishes])
