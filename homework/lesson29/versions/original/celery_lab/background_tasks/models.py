from django.db import models


class EmailNotification(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)
    
    
class LogEntry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class ScrapedPage(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    scraped_at = models.DateTimeField(auto_now_add=True)
    
    
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='upload_images/')
    classification_result = models.CharField(max_length=255, blank=True)
    
    image_type = models.CharField(max_length=20, blank=True)
    image_format = models.CharField(max_length=20, blank=True)
    image_mode = models.CharField(max_length=20, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    orientation = models.CharField(max_length=20, blank=True)
    pixel_count = models.PositiveBigIntegerField(null=True, blank=True)
    has_alpha = models.BooleanField(null=True, blank=True)