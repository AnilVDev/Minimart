from rest_framework import generics, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from django.db import transaction


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                serializer = self.get_serializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {
                            "status": True,
                            "message": "Order created successfully.",
                            "data": serializer.data,
                        },
                        status=status.HTTP_201_CREATED,
                    )
                return Response(
                    {
                        "status": False,
                        "message": "Invalid data provided.",
                        "data": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": f"Error creating order: {str(e)}",
                    "data": None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        try:
            orders = self.get_queryset()
            serializer = self.get_serializer(orders, many=True)
            return Response(
                {
                    "status": True,
                    "message": "Orders fetched successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": f"Error fetching orders: {str(e)}",
                    "data": None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        try:
            order = self.get_object()
            serializer = self.get_serializer(order)
            return Response(
                {
                    "status": True,
                    "message": "Order fetched successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Order.DoesNotExist:
            return Response(
                {"status": False, "message": "Order not found.", "data": None},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": f"Error fetching order: {str(e)}",
                    "data": None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "pk"

    def patch(self, request, *args, **kwargs):
        try:
            order = self.get_object()
            serializer = self.get_serializer(order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": True,
                        "message": "Order updated successfully.",
                        "data": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {
                    "status": False,
                    "message": "Invalid data.",
                    "data": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Order.DoesNotExist:
            return Response(
                {"status": False, "message": "Order not found.", "data": None},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": f"Error updating order: {str(e)}",
                    "data": None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
