from django.db import models

class Comments(models.Model):
    message = models.TextField()