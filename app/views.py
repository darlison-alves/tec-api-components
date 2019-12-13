from rest_framework import generics
from .models import Music
from .serializers import MusicSerializers

class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializers