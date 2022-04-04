from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import CartAddProductForm
from produto.models import Produto


@require_POST
def cart_add(request, produto_id):
    cart = Cart(request)
    produto = get_object_or_404(Produto, id=produto_id)

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            produt=produto, quantidade=cd["quantidade"], override_quantity=cd["override"]
        )

    return redirect("cart:detail")


@require_POST
def cart_remove(request, produto_id):
    cart = Cart(request)
    produto = get_object_or_404(Produto, id=produto_id)
    cart.remove(produto)
    return redirect("cart:detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart.html", {"cart": cart})