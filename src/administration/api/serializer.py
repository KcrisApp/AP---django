from rest_framework import serializers
from rest_framework.serializers import BaseSerializer
from administration.models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        exclude = ["updated_at",'id']
    
