from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)

class CacheManager:
    """
    Centralized Redis wrapper to handle high-concurrency data retrieval.
    Includes logging for 'Cache Hits' vs 'Cache Misses' to monitor performance.
    """
    
    @staticmethod
    def get_or_set_complex_query(key, query_fn, timeout=600):
        """
        Attempts to get data from Redis. If it doesn't exist, executes 
        the query_fn, stores the result, and returns it.
        """
        result = cache.get(key)
        
        if result is not None:
            logger.info(f"CACHE_HIT: Key '{key}' retrieved from Redis.")
            return result
        
        logger.info(f"CACHE_MISS: Key '{key}' not found. Querying Database.")
        # Execute the database query or expensive calculation
        result = query_fn()
        
        # Store in Redis
        cache.set(key, result, timeout=timeout)
        return result

    @staticmethod
    def invalidate_pattern(pattern):
        """Clears all keys matching a specific pattern (e.g., 'analytics_*')"""
        cache.delete_pattern(pattern)
