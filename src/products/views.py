from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProductListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get("slug")
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found...")
        except ProductMultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Hmm")
        return instance


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get("pk")
        instance = Product.objects.get(id=pk)
        if instance is None:
            raise Http404("Product does not exist")
        return instance


def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print("no such product")
    #     raise Http404("Product does not exist")
    # except:
    #     print("huh?")

    qs = Product.objects.filter(id=pk)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Product no existe")

    context = {
        "object": instance
    }
    return render(request, "products/detail.html", context)
