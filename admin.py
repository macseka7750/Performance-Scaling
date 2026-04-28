from django.contrib import admin
from .models import DataPoint

@admin.register(DataPoint)
class DataPointAdmin(admin.ModelAdmin):
    list_display = ('source', 'value', 'timestamp')
    list_filter = ('source', 'timestamp')
    search_fields = ('source', 'metadata')
    date_hierarchy = 'timestamp' # Adds a fast drill-down navigation by date
    list_per_page = 100          # Prevents massive queries in the admin UI
