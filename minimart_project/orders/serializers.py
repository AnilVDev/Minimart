# serializers.py

from rest_framework import serializers
from .models import Order, OrderItem
from customers.models import Customer
from products.models import Product
from django.db import transaction


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["product", "qty"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)
    order_items = OrderItemSerializer(source="orderitem_set", many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "customer", "status", "date", "items", "order_items"]
        read_only_fields = ["id", "date", "order_items"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")

        for item in items_data:
            product = item["product"]
            qty = item["qty"]
            if product.in_stock < qty:
                raise serializers.ValidationError(
                    {
                        "status": False,
                        "message": f"Insufficient stock for product '{product.name}'.",
                        "data": {
                            "product_id": product.id,
                            "available": product.in_stock,
                        },
                    }
                )

        with transaction.atomic():
            order = Order.objects.create(**validated_data)

            for item_data in items_data:
                product = item_data["product"]
                qty = item_data["qty"]
                OrderItem.objects.create(order=order, product=product, qty=qty)
                product.in_stock -= qty
                product.save()

        return order
