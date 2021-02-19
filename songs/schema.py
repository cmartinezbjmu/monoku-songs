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

class SongType(DjangoObjectType):
    class Meta:
        model = Song

# Create a Query type
class Query(ObjectType):
    artist = graphene.Field(ArtistType, id=graphene.Int())
    band = graphene.Field(BandType, id=graphene.Int())
    song = graphene.Field(SongType, id=graphene.Int())
    artists = graphene.List(ArtistType)
    bands= graphene.List(BandType)
    songs= graphene.List(SongType)

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

    def resolve_song(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Band.objects.get(pk=id)

        return None        

    def resolve_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_bands(self, info, **kwargs):
        return Band.objects.all()

    def resolve_songs(self, info, **kwargs):
        return Band.objects.all()        

# Create Input Object Types
class ArtistInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class BandInput(graphene.InputObjectType):
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
        return CreateArtist(ok=ok, actor=artist_instance)

# Create mutations for Song
class CreateSong(graphene.Mutation):
    class Arguments:
        input = ArtistInput(required=True)

    ok = graphene.Boolean()
    artist = graphene.Field(ArtistType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        artist_instance = Artist(name=input.name)
        artist_instance.save()
        return CreateArtist(ok=ok, actor=artist_instance)        

class Mutation(graphene.ObjectType):
    create_artist = CreateArtist.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)    