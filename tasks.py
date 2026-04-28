from celery import shared_task
from django.db.models import Avg
from .models import DataPoint
import time

@shared_task
def process_daily_stats():
    """Simulates a heavy, long-running data aggregation task."""
    # Simulation of a heavy calculation
    time.sleep(5) 
    
    stats = DataPoint.objects.values('source').annotate(average_value=Avg('value'))
    
    # In a real app, you might save these to a 'Summary' table 
    # or send a notification once finished.
    return list(stats)
