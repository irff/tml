from django.db import models
from utils.models import *
from users.models import *

class LibraryManager(models.Manager):
    def create_library(self, user, **extra_fields):
        library = self.model(user=user, **extra_fields)
        library.save()
        return library

class Library(BaseModel):
    user = models.ForeignKey(User)
    objects = LibraryManager()

    def __unicode__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name) + '\'s library'
