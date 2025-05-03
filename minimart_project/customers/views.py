from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer


@api_view(["GET", "POST"])
def customer_list_create(request):
    try:
        if request.method == "GET":
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
            return Response(
                {
                    "status": True,
                    "message": "Customer list retrieved successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        elif request.method == "POST":
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": True,
                        "message": "Customer created successfully.",
                        "data": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                {
                    "status": False,
                    "message": "Validation failed.",
                    "data": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    except Exception as e:
        return Response(
            {
                "status": False,
                "message": f"Something went wrong: {str(e)}",
                "data": None,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET", "PATCH", "DELETE"])
def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(
            {"status": False, "message": "Customer not found.", "data": None},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        if request.method == "GET":
            serializer = CustomerSerializer(customer)
            return Response(
                {
                    "status": True,
                    "message": "Customer retrieved successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        elif request.method == "PATCH":
            serializer = CustomerSerializer(customer, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": True,
                        "message": "Customer updated successfully.",
                        "data": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {
                    "status": False,
                    "message": "Validation failed.",
                    "data": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        elif request.method == "DELETE":
            customer.delete()
            return Response(
                {
                    "status": True,
                    "message": "Customer deleted successfully.",
                    "data": None,
                },
                status=status.HTTP_204_NO_CONTENT,
            )

    except Exception as e:
        return Response(
            {
                "status": False,
                "message": f"Something went wrong: {str(e)}",
                "data": None,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
