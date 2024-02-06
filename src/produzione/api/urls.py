from django.urls import path, include
# from produzione.api.views import OrderViewset,BoardViewSet, BoardListCreateAPIView, BoardDetailAPIView, OrderCreateAPIView, OrderDetailAPIView, OrderListAPIView, SmtCreateAPIView, SmtDetailAPIView, SmtListAPIView, TestCreateAPIView, TestDetailAPIView, TestListAPIView, VerifyCreateAPIView, VerifyDetailAPIView, VerifyListAPIView
from produzione.api.views import BoardImgUpdate, OrderViewset,BoardViewSet, TestListAPIView, TestDetailAPIView, SmtDetailAPIView, SmtListAPIView, VerifyDetailAPIView, VerifyListAPIView, ShippingViewSet, ProductionStepViewset, ProductionListAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"order",OrderViewset)
router.register(r"board",BoardViewSet)
router.register(r"shipping",ShippingViewSet)
router.register(r"productionstep",ProductionStepViewset)



urlpatterns = [
     path("",include(router.urls)),
 
     path("boardImgUpdate/<int:pk>",
         BoardImgUpdate.as_view(),
         name="board-img-update"),
     path("test/",
         TestListAPIView.as_view(),
         name="test-list"),

     path("test/<uuid:uuid>/", 
          TestDetailAPIView.as_view(),
          name="test-details"),


     path("verify/",
          VerifyListAPIView.as_view(),
          name="verify-list"),

     path("verify/<uuid:uuid>/",
          VerifyDetailAPIView.as_view(),
          name="verify-details"),


     path("smt/",
          SmtListAPIView.as_view(),
          name="smt-list"),
     path("smt/<uuid:uuid>/",
          SmtDetailAPIView.as_view(),
          name="smt-details"),


     path("production/<uuid:uuid>/",
          ProductionListAPIView.as_view(),
          name="production-details"),
   
     ]

