from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    ProductListView,
    # product_list_view,
    # ProductDetailView,
    ProductDetailSlugView,
    # product_detail_view,
    # ProductFeaturedListView,
    # ProductFeaturedDetailView,
)

app_name = "products"

urlpatterns = [
    path('', ProductListView.as_view(), name="list"),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name="detail"),
]
