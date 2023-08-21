from rest_framework import viewsets
from ...books.api import serialazers
from ...books import models

class BooksViewSets(viewsets.ModelViewSet):
    serializer_class = serialazers.BooksSerializers
    queryset = models.Books.objects.all()