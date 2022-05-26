from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


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
