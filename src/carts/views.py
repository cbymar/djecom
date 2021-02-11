from django.shortcuts import render
from django.apps import apps
from .models import Cart

# Product = apps.get_model("products", "Product")
# Cart = apps.get_model("carts", "Cart")


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)  # shouldn't this be user=user?
    print("Creating new cart")
    return cart_obj


def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    qs = Cart.objects.filter(id=cart_id)
    if qs.count == 1:
        print("Cart ID exists")
        cart_obj = qs.first()
        if request.user.is_authenticated() and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        # cart_obj = cart_create()  # now that we have a modelManager for Cart, we can:
        cart_obj = Cart.objects.new(user=request.user)
        request.session["cart_id"] = cart_obj.id
    return render(request, "carts/home.html", {})
