from django.core.cache import cache
from .models import Property

def get_all_properties():
    query_set = cache.get('all_properties')

    if not query_set:
        query_set = Property.objects.all()
        cache.set('all_properties', query_set, 3600)
    return query_set