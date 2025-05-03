from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    in_stock = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'cost'], name='unique_product')
        ]

    def __str__(self):
        return f'{self.name} - {self.in_stock}'