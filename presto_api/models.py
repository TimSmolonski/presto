from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    rating = models.IntegerField(blank=False,
                                 null=False,
                                 validators=[MinValueValidator(1), MaxValueValidator(5)],
                                 default=5)

    class Meta:
        verbose_name = 'restaurant'

    def __str__(self):
        return self.title


class Topping(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='sub_toppings')
    cost = models.FloatField(blank=False, default=0.0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.parent and self.parent.id == self.id:
            self.parent = None
        super(Topping, self).save(*args, **kwargs)


class Dish(models.Model):
    name = models.CharField(max_length=32)
    toppings = models.ManyToManyField(Topping, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')
    base_cost = models.FloatField(blank=False, default=0.0)

    class Meta:
        verbose_name = 'dish'
        verbose_name_plural = 'dishes'

    def __str__(self):
        return self.name
