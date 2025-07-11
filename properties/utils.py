from django.core.cache import cache
from .models import Property
import redis
from django.conf import settings
import logging

def get_all_properties():
    query_set = cache.get('all_properties')

    if not query_set:
        query_set = Property.objects.all()
        cache.set('all_properties', query_set, 3600)
    return query_set

logger = logging.getLogger(__name__)
r = redis.Redis(host='redis', port=6379, db=0)

def get_redis_cache_metrics():
    info = r.info('stats')
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)

    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else 0

    metrics = {
        "hits": hits,
        "misses": misses,
        "total_requests": total,
        "hit_ratio": round(hit_ratio, 4)
    }

    logger.info(f"Redis Cache Metrics: {metrics}")

    return metrics
        