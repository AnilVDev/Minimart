from django.urls import path
from .views import OrderCreateView, OrderListView, OrderDetailView, OrderUpdateView

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='order-delete'),
]