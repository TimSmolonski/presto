from django.urls import include, path
from rest_framework_nested import routers

from .views import RestaurantViewSet, DishViewSet, ToppingViewSet, RestaurantItemViewSet

router = routers.DefaultRouter()

router.register(r'restaurants', RestaurantViewSet, base_name='restaurants')

restaurant_dishes_router = routers.NestedSimpleRouter(router, r'restaurants', lookup='restaurant')
restaurant_dishes_router.register(r'item', RestaurantItemViewSet, base_name='restaurant-item')
router.register(r'dishes', DishViewSet, base_name='dishes')
router.register(r'toppings', ToppingViewSet, base_name='toppings')

urlpatterns = [
    path('', include(router.urls)),
    path(r'', include(restaurant_dishes_router.urls))
]
