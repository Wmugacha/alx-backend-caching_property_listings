from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.core import serializers
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all()
    data = serializers.serialize('json', properties)
    return JsonResponse(data, safe=False)