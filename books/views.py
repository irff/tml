from rest_framework import viewsets
from rest_framework.decorators import detail_route
from books.models import *
from books.serializers import *

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer