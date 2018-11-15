from rest_framework import viewsets

from .models import Restaurant, Dish, Topping
from .serializers import RestaurantSerializer, DishSerializer, ToppingSerializer


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class DishViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class ToppingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
