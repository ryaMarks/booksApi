from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .books.api import viewsets as boooksviewsets

route = routers.DefaultRouter()
route.register('books', boooksviewsets.BooksViewSets, basename='Books')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(route.urls)),
    
]
