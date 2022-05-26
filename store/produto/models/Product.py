from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from produto.models.AvailableManager import AvailableManager

from produto.models.Category import Category

class Product(models.Model):

    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    image = models.ImageField(upload_to="produto//%Y/%m/%d", blank=True)
    descricao = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("produto:detail", kwargs={"slug": self.slug})
