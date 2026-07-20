from django.db import models


class Report(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("RUNNING", "Running"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    ]

    status = models.CharField(max_length=20, 
                              choices=STATUS_CHOICES,
                              default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Report {self.id} - {self.status}"
    
    
class Ping(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Ping {self.id} - {self.created_at}"