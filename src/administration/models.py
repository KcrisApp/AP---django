from django.db import models
import uuid as uuid_lib
from core.models import TimeStampedModel
from django_quill.fields import QuillField
# Create your models here.
class Announcement(TimeStampedModel):
     
    TYPE_CHOICES = ( 
        ('comunicato', "comunicato"), 
        ('avviso', "avviso"), 
    )

    uuid = models.UUIDField(default=uuid_lib.uuid4 ,editable=False)
    announcement_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default="comunicato")
    announcement_title = models.CharField(max_length=50, default="", null=False)
    announcement_content = QuillField()

    def __str__(self):
       
        return f'{self.created_at} - {self.announcement_title}'
    
    
    class Meta:

        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"