# from django.db import models

# class Customer(models.Model):
#     full_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=255)

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     cost = models.FloatField()
#     in_stock = models.IntegerField()

# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     qty = models.IntegerField()