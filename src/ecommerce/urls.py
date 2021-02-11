"""
ecommerce URL Configuration
https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


from .views import home_page, about_page, contact_page, login_page, register_page

from carts.views import cart_home

urlpatterns = [
    path('', home_page, name="home"),
    path('about/', about_page, name="about"),
    path('contact/', contact_page, name="contact"),
    path('login/', login_page, name="login"),
    path('cart/', cart_home, name="cart"),
    path('register/', register_page, name="register"),
    path('bootstrap/', TemplateView.as_view(template_name="bootstrap/example.html")),
    path('products/', include("products.urls", namespace="products")),
    path('search/', include("search.urls", namespace="search")),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
