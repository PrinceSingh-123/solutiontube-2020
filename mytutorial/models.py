from django.db import models

# Create your models here.
class Solution_videos(models.Model):
    name = models.CharField(max_length=100)
    video_link = models.URLField(null=True)

    def __str__(self):
        return self.name
        