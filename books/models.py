from utils.models import *

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

    class Meta:
        ordering = ('created_at',)