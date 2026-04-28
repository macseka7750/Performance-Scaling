from django.db import models

class DataPoint(models.Model):
    """Represents a high-volume data entry for analytics processing."""
    source = models.CharField(max_length=100)
    value = models.FloatField()
    metadata = models.JSONField(default=dict)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True) # Index for fast time-series queries

    class Meta:
        ordering = ['-timestamp']
        # Professional Touch: Indexing for common filter combinations
        indexes = [
            models.Index(fields=['source', '-timestamp']),
        ]

    def __str__(self):
        return f"{self.source}: {self.value}"
