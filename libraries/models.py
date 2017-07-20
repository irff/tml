from django.db import models
from utils.models import *
from books.models import *

class Library(BaseModel):
    user = models.OneToOneField()
    books = models.ManyToManyField(Book)

    def __unicode__(self):
        return self.user.name + '\'s Library'
