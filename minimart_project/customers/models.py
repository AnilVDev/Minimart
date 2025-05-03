from django.db import models


class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.full_name
