from django.db import models

from carts.models import *
from utils.models import *

class OrderManager(models.Manager):
    def create_order(self, cart, delivery_date=None, **extra_fields):
        order = self.model(cart=cart, delivery_date=delivery_date, **extra_fields)
        order.save()
        return order

class OrderLineManager(models.Manager):
    def create_order_line(self, cart_line, order, **extra_fields):
        order_line = self.model(cart_line=cart_line, order=order, **extra_fields)
        order_line.save()
        return order_line

class Order(BaseModel):
    delivery_date = models.DateField(blank=True, null=True, db_index=True)
    address = models.TextField()
    cart = models.OneToOneField(Cart, related_name='order')
    library = models.ForeignKey(Library, related_name='orders')

    objects = OrderManager()

    def __unicode__(self):
        return

    class Meta:
        ordering = ['-created_at']

class OrderLine(BaseModel):
    cart_line = models.OneToOneField(CartLine, related_name='order_line')
    delivered_by = models.DateField(blank=True, null=True)
    is_delivered = models.BooleanField(default=False)
    order = models.ForeignKey(Order, related_name='order_lines')

    objects = OrderLineManager()

    def __unicode__(self):
        return str(self.cart_line)

    class Meta:
        ordering = ['-created_at']