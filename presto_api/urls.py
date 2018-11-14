from django.urls import include, path
from rest_framework import routers
from .views import RestaurantViewSet


router = routers.DefaultRouter()

router.register(r'restaurants', RestaurantViewSet, base_name='restaurants')

urlpatterns = [
    path('', include(router.urls))
]
