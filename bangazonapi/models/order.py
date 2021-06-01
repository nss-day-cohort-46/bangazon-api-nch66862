"""Customer order model"""
from .orderproduct import OrderProduct
from django.db import models
from .customer import Customer
from .payment import Payment


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING,)
    payment_type = models.ForeignKey(Payment, on_delete=models.DO_NOTHING, null=True)
    created_date = models.DateField(default="0000-00-00",)

    @property
    def total_cost(self):
        """Average rating calculated attribute for each product

        Returns:
            number -- The average rating for the product
        """
        line_items = OrderProduct.objects.filter(order=self)
        total_cost = 0
        for item in line_items:
            total_cost += item.product.price
        return total_cost
