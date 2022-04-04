from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse



class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    class Meta:
        ordering = ("nome",)
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("produto:list_by_category", kwargs={"slug": self.slug})


class Produto(models.Model):
    categoria = models.ForeignKey(
        Categoria, related_name="produto", on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    image = models.ImageField(upload_to="produto/%Y/%m/%d", blank=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    # available = AvailableManager()

    class Meta:
        ordering = ("nome",)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("produto:detail", kwargs={"slug": self.slug})