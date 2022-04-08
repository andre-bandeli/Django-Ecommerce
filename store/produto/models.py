from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)

class Category(models.Model):

    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("produto:list_by_category", kwargs={"slug": self.slug})


class Product(models.Model):

    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
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


class ProductHome(models.Model):

    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")
    image = models.ImageField(upload_to="produto/%Y/%m/%d", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("producto:detail", kwargs={"slug": self.slug})
