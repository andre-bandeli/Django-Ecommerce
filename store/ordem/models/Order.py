
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from localflavor.br.models import BRCPFField, BRPostalCodeField, BRStateField
from produto.models.Product import Product



class Order(models.Model):
    cpf = BRCPFField("CPF")
    name = models.CharField("Nome Completo", max_length=250)
    email = models.EmailField()
    postal_code = BRPostalCodeField("CEP")
    address = models.CharField("Endereço", max_length=250)
    number = models.CharField("Número", max_length=250)
    complement = models.CharField("Complemento", max_length=250, blank=True)
    district = models.CharField("Bairro", max_length=250)
    state = BRStateField("Estado")
    city = models.CharField("Cidade", max_length=250)
    paid = models.BooleanField(default=False)


    def __str__(self):
        return f"Pedido {self.id}"

