from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

from produto.models.Category import Category


class SubCategory(models.Model):

    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    category = models.ForeignKey(
            Category, related_name="subcategory", on_delete=models.CASCADE
    )
    class Meta:
        ordering = ("name",)
        verbose_name = "subcategorie"
        verbose_name_plural = "sub-Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("produto:list_by_category", kwargs={"slug": self.slug})
