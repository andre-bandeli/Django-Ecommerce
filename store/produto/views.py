from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView


from .models import Categoria, Produto, ProdutoAmostra


class home(ListView):

    def get_queryset(self):
        queryset = ProdutoAmostra.available.all()
        return queryset

class list_produtos(ListView):

    categoria = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Produto.available.all()
        categoria_slug = self.kwargs.get("slug")

        if categoria_slug:
            self.categoria = get_object_or_404(Categoria, slug=categoria_slug)
            queryset = queryset.filter(categoria=self.categoria)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categoria"] = self.categoria
        context["categorias"] = Categoria.objects.all()
        return context

class ProductDetailView(DetailView):
    queryset = Produto.available.all()
    # extra_context = {"form": CartAddProductForm()}

