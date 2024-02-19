from rest_framework import serializers
from rest_framework.serializers import BaseSerializer
from administration.models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        exclude = ["updated_at",'id']
    
    def get_html(self, instance):
            return str(instance.announcement_content.html)