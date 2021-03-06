from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Restaurant, Dish, Topping


class ToppingSerializer(serializers.ModelSerializer):
    sub_toppings = serializers.ListSerializer(read_only=True, child=RecursiveField())

    class Meta:
        model = Topping
        fields = ('name',  'cost', 'sub_toppings')


class DishSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True)

    class Meta:
        model = Dish
        fields = ('name', 'base_cost', 'toppings')


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('title', 'address', 'rating')
