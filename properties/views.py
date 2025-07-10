from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.core import serializers
from .models import Property
from .serializers import PropertySerializer

@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return JsonResponse({"data": serializer.data})