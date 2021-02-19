"""Songs models admin."""

from django.contrib import admin
from .models import Artist, Band, Album, Genre, Subgenre, Song

# Register your models here.
models = [Artist, Band, Album, Genre, Subgenre, Song]
admin.site.register(models)