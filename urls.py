from django.urls import path
from .views import TriggerAnalyticsView

urlpatterns = [
    path('process/', TriggerAnalyticsView.as_view(), name='trigger-analytics'),
]
