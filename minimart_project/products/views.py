from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductListCreate(APIView):
    def get(self, request):
        try:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(
                {
                    "status": True,
                    "message": "Products retrieved successfully.",
                    "data": serializer.data,
                }
            )
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": f"Error fetching products: {str(e)}",
                    "data": None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": True,
                        "message": "Product created successfully.",
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
                    "message": f"Error creating product: {str(e)}",
                    "data": None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None
        except Exception as e:
            raise Exception(f"Error retrieving product: {str(e)}")

    def get(self, request, pk):
        try:
            product = self.get_object(pk)
            if product:
                serializer = ProductSerializer(product)
                return Response(
                    {
                        "status": True,
                        "message": "Product retrieved successfully.",
                        "data": serializer.data,
                    }
                )
            return Response(
                {"status": False, "message": "Product not found.", "data": None},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": f"Error retrieving product: {str(e)}",
                    "data": None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def patch(self, request, pk):
        try:
            product = self.get_object(pk)
            if product:
                serializer = ProductSerializer(product, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {
                            "status": True,
                            "message": "Product updated successfully.",
                            "data": serializer.data,
                        }
                    )
                return Response(
                    {
                        "status": False,
                        "message": "Invalid data provided.",
                        "data": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(
                {"status": False, "message": "Product not found.", "data": None},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": f"Error updating product: {str(e)}",
                    "data": None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, request, pk):
        try:
            product = self.get_object(pk)
            if product:
                product.delete()
                return Response(
                    {
                        "status": True,
                        "message": "Product deleted successfully.",
                        "data": None,
                    },
                    status=status.HTTP_204_NO_CONTENT,
                )
            return Response(
                {"status": False, "message": "Product not found.", "data": None},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": f"Error deleting product: {str(e)}",
                    "data": None,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
