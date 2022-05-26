from urllib import request

from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from cart.cart import Cart
from cart.forms import CartAddProductForm
from produto.models.Category import Category
from produto.models.Product import Product
from produto.models.ProductHomeList import ProductHomeList

# Página Index [home]
def home(request):
    data = {}
    data['db'] = Product.objects.all()
    data['categories'] = Category.objects.all()
    data["produto_list"] = ProductHomeList.objects.all()

    return (render(request, 'produto/home.html', data))

# Página de Detalhar Produtos
class ProductDetailView(DetailView):
    queryset = Product.available.all()
    extra_context = {"form": CartAddProductForm()}

# Página de Listar Produtos
class ProductListView(ListView):
    category = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.available.all()
        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context

