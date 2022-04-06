import copy
from decimal import Decimal

from django.conf import settings


from .forms import CartAddProductForm
from produto.models import Produto


class Cart:
    def __init__(self, request):
        if request.session.get(settings.CART_SESSION_ID) is None:
            request.session[settings.CART_SESSION_ID] = {}

        self.cart = request.session[settings.CART_SESSION_ID]
        self.session = request.session

    def __iter__(self):
        cart = copy.deepcopy(self.cart)

        products = Produto.objects.filter(id__in=cart)
        for product in products:
            cart[str(product.id)]["produto"] = product

        for item in cart.values():
            item["preco"] = Decimal(item["preco"])
            item["preco_total"] = item["quantidade"] * item["preco"]
            item["update_quantity_form"] = CartAddProductForm(
                initial={"quantidade": item["quantidade"], "override": True}
            )

            yield item

    def __len__(self):
        return sum(item["quantidade"] for item in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(product.price),
            }

        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        self.cart[product_id]["quantity"] = min(20, self.cart[product_id]["quantity"])

        self.save()

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True