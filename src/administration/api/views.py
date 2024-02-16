from django.shortcuts import get_object_or_404

from rest_framework import permissions
from rest_framework import viewsets

from administration.api.permissions import IsManagerOrReadOnly
from administration.models import Announcement
from .serializer import AnnouncementSerializer

# Orders views V2
class AnnouncementView(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsManagerOrReadOnly]
    lookup_field = "uuid"

