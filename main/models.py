from django.db import models
from django.conf import settings

class UserPageVisit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    visited_at = models.DateTimeField(auto_now_add=True)
    page_visited = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.username} посетил {self.page_visited} ({self.visited_at})"