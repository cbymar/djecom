from django.shortcuts import render, redirect
from django.apps import apps
from .models import Cart
from products.models import Product
# Product = apps.get_model("products", "Product")
# Cart = apps.get_model("carts", "Cart")


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # cart_obj, new_obj = Cart.objects.new_or_get(request)
    # products = cart_obj.products.all()
    # total = 0
    # for x in products:
    #     total += x.price
    # print(total)
    # cart_obj.total = total
    # cart_obj.save()
    return render(request, "carts/home.html", {})


def cart_update(request):
    """
    Add a product to the cart.  Updates cart and returns to the view of the product
    """
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)

    return redirect("cart:home")