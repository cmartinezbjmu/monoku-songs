"""Songs serializers"""

# Django Rest Framework
from rest_framework import serializers

# Models
from .models import Artist, Band, Album, Genre, Subgenre, Song


class ArtistSerializer(serializers.ModelSerializer):
    """Artist serializer."""
    class Meta:
        model = Artist
        fields = "__all__"

class BandSerializer(serializers.ModelSerializer):
    """Band serializer."""
    class Meta:
        model = Band
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    """Album serializer."""
    class Meta:
        model = Album
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    """Genre serializer."""
    class Meta:
        model = Genre
        fields = "__all__"

class SubgenreSerializer(serializers.ModelSerializer):
    """Subgenre serializer."""
    class Meta:
        model = Subgenre
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):
    """Song serializer."""
    class Meta:
        model = Song
        fields = "__all__"                