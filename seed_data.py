import os
import django
import random
from datetime import datetime, timedelta
from django.utils import timezone

# 1. Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.analytics.models import DataPoint

def seed_performance_data(count=100000):
    """
    Injects a large volume of data using bulk_create.
    This demonstrates how the system handles heavy indexing and 
    complex time-series queries.
    """
    print(f"--- Starting Seed Process: {count} rows ---")
    
    sources = ['sensor_a', 'sensor_b', 'api_gateway', 'mobile_client', 'web_frontend']
    batch_size = 5000
    objs = []
    
    start_time = timezone.now() - timedelta(days=30)

    for i in range(count):
        # Create a randomized data point
        objs.append(
            DataPoint(
                source=random.choice(sources),
                value=random.uniform(10.0, 500.0),
                metadata={
                    "version": "1.2.0",
                    "region": random.choice(["US-East", "EU-West", "AP-South"]),
                    "load_factor": random.random()
                },
                # Distribute timestamps over the last 30 days
                timestamp=start_time + timedelta(seconds=random.randint(0, 2592000))
            )
        )

        # Bulk insert in batches to manage memory usage
        if len(objs) >= batch_size:
            DataPoint.objects.bulk_create(objs)
            objs = []
            print(f"Inserted {i + 1} rows...")

    # Final batch
    if objs:
        DataPoint.objects.bulk_create(objs)

    print(f"--- Seeding Complete: {count} rows added in {timezone.now() - start_time} ---")

if __name__ == "__main__":
    seed_performance_data()
