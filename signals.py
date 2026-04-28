from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import DataPoint

@receiver(post_save, sender=DataPoint)
def clear_analytics_cache(sender, instance, **kwargs):
    """
    Automatically clears the Redis cache whenever a new data point is added.
    This ensures our 'High-Performance' engine never serves outdated stats.
    """
    cache.delete('global_analytics_summary')
