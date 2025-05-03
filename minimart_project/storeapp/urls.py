from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path('customers/', include('customers.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
]
