
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import process_daily_stats

class TriggerAnalyticsView(APIView):
    def post(self, request):
        # .delay() sends the task to the Redis queue and returns immediately
        task = process_daily_stats.delay()
        
        return Response({
            "message": "Analytics processing started in background.",
            "task_id": task.id
        })
