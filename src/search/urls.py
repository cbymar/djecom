from django.urls import path

from .views import SearchProductView
from products.views import (
    ProductListView
)

app_name = "search"

urlpatterns = [
    path('', SearchProductView.as_view(), name="query"),
]
