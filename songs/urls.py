"""Songs urls."""

# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework import routers

# Views
from .views import ArtistViewSet, BandViewSet, AlbumViewSet, GenreViewSet, SubgenreViewSet, SongViewSet

router = routers.DefaultRouter()

router.register(r"artists", ArtistViewSet, basename="artists")
router.register(r"bands", BandViewSet, basename="bands")
router.register(r"albums", AlbumViewSet, basename="albums")
router.register(r"genres", GenreViewSet, basename="genres")
router.register(r"subgenres", SubgenreViewSet, basename="subgenres")
router.register(r"songs", SongViewSet, basename="songs")

urlpatterns = [    
    path("", include(router.urls)),
]