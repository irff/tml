from django.db import models
from utils.models import *
from users.models import *
from books.models import *

class CartManager(models.Manager):
    def create_cart(self,user, **extra_fields):
        cart = self.model(user=user, **extra_fields)
        cart.save()
        return cart

class CartLineManager(models.Manager):
    def create_cart_line(self, book_record, library, cart, **extra_fields):
        cart_line = self.model(book_record=book_record, library=library, cart=cart, **extra_fields)
        cart_line.save()
        return cart_line

class Cart(BaseModel):
    user = models.ForeignKey(User)

    objects = CartManager()

    class Meta:
        ordering = ('created_at',)

class CartLine(BaseModel):
    book_record = models.ForeignKey(BookRecord)
    library = models.ForeignKey(Library)
    cart = models.ForeignKey(Cart)

    def __unicode__(self):
        return str(self.book_record.book.title)

    class Meta:
        ordering = ('created_at',)