
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from ordem.models.Order import Order
from produto.models.Product import Product


class Item(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="self", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(20),
        ]
    )

    def __str__(self):
        return str(self.id)