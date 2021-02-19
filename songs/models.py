"""Songs models."""

# Django
from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    
    class Meta:
        """Table name."""
        db_table = 'artist'

class Band(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="band_artist")

    class Meta:
        """Table name."""
        db_table = 'band'

class Album(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name="album_band")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="album_artist")

    class Meta:
        """Table name."""
        db_table = 'album'


class Genre(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

    class Meta:
        """Table name."""
        db_table = 'genre'

class Subgenre(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

    class Meta:
        """Table name."""
        db_table = 'subgenre'


class Song(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    duration = models.CharField(max_length=10, blank=False, null=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="song_album")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="song_genre")
    subgenre = models.ForeignKey(Subgenre, on_delete=models.CASCADE, related_name="song_subgenre")
    similar_band = models.ManyToManyField(Band, related_name="similar_band_song")

    class Meta:
        """Table name."""
        db_table = 'song'

