from django.db import models
from utils.models import *
from users.models import *
from libraries.models import *

class BookRecordManager(models.Manager):
    def create_book_record(self, book, library, **extra_fields):
        book_record = self.model(book=book, library=library, **extra_fields)
        book_record.save()
        return book_record

class AuthorManager(models.Manager):
    def create_author(self, name, **extra_fields):
        author = self.model(name=name, **extra_fields)
        author.save()
        return author

class BookManager(models.Manager):
    def create_book(self, title, authors, description, year_published, image, language, **extra_fields):
        book = self.model(title=title, description=description, year_published=year_published, image=image, language=language, **extra_fields)
        book.save()

        for author in authors:
            book.authors.add(author)

        return book

class Author(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class Book(BaseModel):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    description = models.TextField(blank=True, null=True)
    year_published = models.DateField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    ENGLISH = 'EN'
    INDONESIAN = 'ID'

    LANGUAGE_CHOICES = (
        (ENGLISH, 'English'),
        (INDONESIAN, 'Indonesian')
    )

    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default=ENGLISH
    )

    objects = BookManager()

    def __unicode__(self):
        return str(self.title)

    class Meta:
        ordering = ('created_at',)

class BookRecord(BaseModel):
    book = models.ForeignKey(Book)
    library = models.ForeignKey(Library)

    AVAILABLE, UNAVAILABLE = 'available', 'unavailable'

    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (UNAVAILABLE, 'Unavailable')
    )

    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default=AVAILABLE
    )

    objects = BookRecordManager()

    def __unicode__(self):
        return str(self.library.user.first_name) + '\'s book: %s'.format(self.book.title)