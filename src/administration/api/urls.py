from django.urls import path, include
# from produzione.api.views import OrderViewset,BoardViewSet, BoardListCreateAPIView, BoardDetailAPIView, OrderCreateAPIView, OrderDetailAPIView, OrderListAPIView, SmtCreateAPIView, SmtDetailAPIView, SmtListAPIView, TestCreateAPIView, TestDetailAPIView, TestListAPIView, VerifyCreateAPIView, VerifyDetailAPIView, VerifyListAPIView
from administration.api.views import AnnouncementView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"announcement", AnnouncementView)


urlpatterns = [
     path("",include(router.urls)),
 
     ]

