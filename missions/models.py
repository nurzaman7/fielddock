from django.db import models

class Mission(models.Model):
    mission_name = models.CharField(max_length=100)
    waypoint_data = models.TextField()  # Store the QGroundControl .wpl content as JSON or plain text
    start_time = models.DateTimeField(auto_now_add=True)
    field_name = models.CharField(max_length=50)  # Additional field for field name

    def __str__(self):
        return self.mission_name

