from django.db import models

# Create your models here.


class ApplicationData(models.Model):
    timestamp = models.CharField(max_length=200)
    data_point = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
