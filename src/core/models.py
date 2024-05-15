from django.db import models
from users.models import CustomUser

# Time stamp model
class TimeStampedModel(models.Model):

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


#Log sys 
class DataLog(TimeStampedModel):
    
    http_request_methods = models.CharField(max_length=10)
    operation_type = models.CharField(max_length=50)
    action = models.CharField(default="", max_length=120)
    message = models.TextField(default="",max_length=250)
  
    
    

    def __str__(self):
        return self.action
    
    class Meta:

        verbose_name = "DataLog"
        verbose_name_plural = "DataLog"
        ordering = ['created_at']