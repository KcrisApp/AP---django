from django.db import models

# Time stamp model
class TimeStampedModel(models.Model):

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


# Log sys 
# class Logger(TimeStampedModel):
#     pass