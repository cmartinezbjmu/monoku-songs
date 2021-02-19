"""Songs views."""

# Django Rest Framework
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
import rest_framework.status as status_codes
from rest_framework.decorators import api_view

# Serializers
from .serializers import ArtistSerializer, BandSerializer, AlbumSerializer, GenreSerializer, SubgenreSerializer, SongSerializer

# Models
from .models import Artist, Band, Album, Genre, Subgenre, Song


class ArtistViewSet(ModelViewSet):
    """Artist ViewSet."""

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class BandViewSet(ModelViewSet):
    """Band ViewSet."""

    queryset = Band.objects.all()
    serializer_class = BandSerializer  


class AlbumViewSet(ModelViewSet):
    """Artist ViewSet."""

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class GenreViewSet(ModelViewSet):
    """Genre ViewSet."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class SubgenreViewSet(ModelViewSet):
    """Subgenre ViewSet."""

    queryset = Subgenre.objects.all()
    serializer_class = SubgenreSerializer

class SongViewSet(ModelViewSet):
    """Song ViewSet."""
    
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre', 'subgenre', 'similar_band', 'album__band', 'album__artist']