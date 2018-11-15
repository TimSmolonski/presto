from django.urls import include, path
from rest_framework import routers
from .views import RestaurantViewSet, DishViewSet, ToppingViewSet

router = routers.DefaultRouter()

router.register(r'restaurants', RestaurantViewSet, base_name='restaurants')
router.register(r'dishes', DishViewSet, base_name='dishes')
router.register(r'toppings', ToppingViewSet, base_name='toppings')

urlpatterns = [
    path('', include(router.urls))
]
