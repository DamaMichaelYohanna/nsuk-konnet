from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    """class for a single product."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(null=True)
    price = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} posted by {self.owner}'


class Store(models.Model):
    """model for stores/shops """
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="store")
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True, max_length=200)
    coordinate = models.CharField(default="(0, 0)", max_length=20)
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Catalog(models.Model):
    """catalogue for none store owner to publish their goods"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Product)


class Order(models.Model):
    """model for single order. with customer and goods added."""
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=12,
                              choices=(("pending", "pending"),
                                       ("processing", "processing"),
                                       ("Done", "Done")),
                              default="pending")

    def __str__(self):
        return f'{self.customer} ordered for {self.product}'


class StoreOrder(models.Model):
    """model for order to a particular store"""
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    order = models.ManyToManyField(Order)

    def __str__(self):
        return f'{self.store}'
