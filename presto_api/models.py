from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=32)
    address = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'restaurant'

    def __str__(self):
        return self.title


class Topping(models.Model):
    name = models.CharField(max_length=32)
    sub_toppings = models.ManyToManyField('self', blank=True, null=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=32)
    toppings = models.ManyToManyField(Topping, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')

    class Meta:
        verbose_name = 'dish'
        verbose_name_plural = 'dishes'

    def __str__(self):
        return self.name