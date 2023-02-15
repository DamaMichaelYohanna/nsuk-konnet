from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    """class for a single product."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)
    created_on = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.name} posted by {self.owner}'
