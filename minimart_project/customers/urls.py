from django.urls import path
from .views import customer_detail,customer_list_create

urlpatterns = [
    path('customers/', customer_list_create, name='customer-list-create'),
    path('customers/<int:pk>/', customer_detail, name='customer-detail'),
]
