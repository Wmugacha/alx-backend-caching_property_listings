from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer


class PropertyListView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer