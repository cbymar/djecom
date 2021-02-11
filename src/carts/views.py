from django.shortcuts import render
from django.apps import apps
from .models import Cart

# Product = apps.get_model("products", "Product")
# Cart = apps.get_model("carts", "Cart")


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # products = cart_obj.products.all()
    # total = 0
    # for x in products:
    #     total += x.price
    # print(total)
    # cart_obj.total = total
    cart_obj.save()
    return render(request, "carts/home.html", {})
