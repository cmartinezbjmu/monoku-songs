"""Songs schemas."""

import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Artist, Band, Album, Genre, Subgenre, Song

# Create a GraphQL type for the artist model
class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist

# Create a GraphQL type for the band model
class BandType(DjangoObjectType):
    class Meta:
        model = Band
        filter_fields = {
            'similar_band': ['exact', 'icontains', 'istartswith'],
            'band': ['exact', 'icontains', 'istartswith']
        }        

# Create a GraphQL type for the album model
class AlbumType(DjangoObjectType):
    class Meta:
        model = Album

# Create a GraphQL type for the song model
class SongType(DjangoObjectType):
    class Meta:
        model = Song

# Create a GraphQL type for the genre model
class GenreType(DjangoObjectType):
    class Meta:
        model = Genre
        filter_fields = {
            'genre': ['exact', 'icontains', 'istartswith']
        }        

# Create a GraphQL type for the subgenre model
class SubgenreType(DjangoObjectType):
    class Meta:
        model = Subgenre                
        filter_fields = {
            'subgenre': ['exact', 'icontains', 'istartswith']
        }  


# Create a Query type
class Query(ObjectType):
    artist = graphene.Field(ArtistType, id=graphene.Int())
    band = graphene.Field(BandType, id=graphene.Int())
    album = graphene.Field(AlbumType, id=graphene.Int())
    song = graphene.Field(SongType, id=graphene.Int())
    genre = graphene.Field(GenreType, id=graphene.Int())
    subgenre = graphene.Field(SubgenreType, id=graphene.Int())
    
    artists = graphene.List(ArtistType)
    bands= graphene.List(BandType)
    album= graphene.List(AlbumType)
    songs= graphene.List(SongType, genre=graphene.ID(), subgenre=graphene.ID(), similar_band=graphene.ID(), band=graphene.ID())
    genres= graphene.List(GenreType)
    subgenres= graphene.List(SubgenreType)

    def resolve_artist(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Artist.objects.get(pk=id)

        return None

    def resolve_band(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Band.objects.get(pk=id)

        return None

    def resolve_album(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Album.objects.get(pk=id)

        return None

    def resolve_song(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Song.objects.get(pk=id)

        return None

    def resolve_genre(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Genre.objects.get(pk=id)

        return None    

    def resolve_subgenre(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Subgenre.objects.get(pk=id)

        return None                                    

    def resolve_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_bands(self, info, **kwargs):
        return Band.objects.all()

    def resolve_albums(self, info, **kwargs):
        return Album.objects.all()

    def resolve_songs(self, info, genre=None, subgenre=None, similar_band=None, band=None, **kwargs):
        if genre:            
            return Song.objects.filter(genre__id=genre)
        if subgenre:            
            return Song.objects.filter(subgenre__id=subgenre)
        if similar_band:            
            return Song.objects.filter(similar_band__id=similar_band)
        if band:            
            return Song.objects.filter(band__id=band)                        
        return Song.objects.all()
           
    def resolve_genres(self, info, **kwargs):
        return Genre.objects.all()    

    def resolve_subgenres(self, info, **kwargs):
        return Subgenre.objects.all()    

# Create Input Object Types
class ArtistInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class BandInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class AlbumInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class SongInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

# Create mutations for Artist
class CreateArtist(graphene.Mutation):
    class Arguments:
        input = ArtistInput(required=True)

    ok = graphene.Boolean()
    artist = graphene.Field(ArtistType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        artist_instance = Artist(name=input.name)
        artist_instance.save()
        return CreateArtist(ok=ok, artist=artist_instance)

# Create mutations for Song
class CreateSong(graphene.Mutation):
    class Arguments:
        input = SongInput(required=True)

    ok = graphene.Boolean()
    artist = graphene.Field(SongType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        song_instance = Song(name=input.name)
        song_instance.save()
        return CreateSong(ok=ok, actor=song_instance)        

class Mutation(graphene.ObjectType):
    create_artist = CreateArtist.Field()
    create_song = CreateSong.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)    