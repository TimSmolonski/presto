from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Restaurant, Dish, Topping


class ToppingSerializer(serializers.ModelSerializer):
    sub_toppings = serializers.ListSerializer(read_only=True, child=RecursiveField())

    class Meta:
        model = Topping
        fields = ('name', 'sub_toppings', 'cost')


class DishSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True)

    class Meta:
        model = Dish
        fields = ('name', 'toppings', 'base_cost')


class RestaurantSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('title', 'address', 'dishes', 'rating')
