from locust import HttpUser, task, between

class AnalyticsLoadTester(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def view_cached_summary(self):
        """Simulates users hitting the Redis-cached endpoint."""
        self.client.get("/api/v1/analytics/summary/")

    @task(1)
    def trigger_background_task(self):
        """Simulates users triggering heavy Celery jobs."""
        self.client.post("/api/v1/analytics/process/")
