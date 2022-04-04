import copy
from decimal import Decimal

from django.conf import settings
from produto.models import Produto
from .forms import CartAddProductForm



class Cart:
    def __init__(self, request):
        if request.session.get(settings.CART_SESSION_ID) is None:
            request.session[settings.CART_SESSION_ID] = {}

        self.cart = request.session[settings.CART_SESSION_ID]
        self.session = request.session

    def __iter__(self):
        cart = copy.deepcopy(self.cart)

        produto = Produto.objects.filter(id__in=cart)
        for produtos in produto:
            cart[str(produtos.id)]["product"] = produtos

        for item in cart.values():
            item["preco"] = Decimal(item["price"])
            item["preco_total"] = item["quantidade"] * item["preco"]
            item["update_quantidade_form"] = CartAddProductForm(
                initial={"quantidade": item["quantity"], "override": True}
            )

            yield item

    def __len__(self):
        return sum(item["quantidade"] for item in self.cart.values())

    def add(self, produto, quantidade=1, override_quantity=False):
        produto_id = str(produto.id)

        if produto_id not in self.cart:
            self.cart[produto_id] = {
                "quantidade": 0,
                "price": str(produto.price),
            }

        if override_quantity:
            self.cart[produto_id]["quantidade"] = quantidade
        else:
            self.cart[produto_id]["quantidade"] += quantidade

        self.cart[produto_id]["quantidade"] = min(20, self.cart[produto_id]["quantidade"])

        self.save()

    def remove(self, produto):
        produto_id = str(produto.id)

        if produto_id in self.cart:
            del self.cart[produto_id]
            self.save()

    def get_total_price(self):
        return sum(
            Decimal(item["preco"]) * item["quantidade"] for item in self.cart.values()
        )

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True