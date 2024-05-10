from django.urls import path, include
# from produzione.api.views import OrderViewset,BoardViewSet, BoardListCreateAPIView, BoardDetailAPIView, OrderCreateAPIView, OrderDetailAPIView, OrderListAPIView, SmtCreateAPIView, SmtDetailAPIView, SmtListAPIView, TestCreateAPIView, TestDetailAPIView, TestListAPIView, VerifyCreateAPIView, VerifyDetailAPIView, VerifyListAPIView
from produzione.api.views import OrderSchematicsFileView, OrderOdbFileView, OrderGerberFileView, OrderStatusViewset, OrderTopographicView, BoardImgUpdateBot, WeldingListAPIView, WeldingDetailAPIView, BoardImgUpdate, OrderViewset,BoardViewSet, TestListAPIView, TestDetailAPIView, SmtDetailAPIView, SmtListAPIView, VerifyDetailAPIView, VerifyListAPIView, ShippingViewSet, ProductionStepViewset, ProductionListAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"order",OrderViewset)
router.register(r"order_status",OrderStatusViewset)
router.register(r"board",BoardViewSet)
router.register(r"shipping",ShippingViewSet)
router.register(r"productionstep",ProductionStepViewset)



urlpatterns = [
     path("",include(router.urls)),
 
     path("boardImgUpdate/<int:pk>",
         BoardImgUpdate.as_view(),
         name="board-img-update"),
     path("boardImgUpdateBot/<int:pk>",
         BoardImgUpdateBot.as_view(),
         name="board-img-update-bot"),
     path("topographicOrder/<int:pk>",
         OrderTopographicView.as_view(),
         name="topographic-file-update"),
     path("odbOrder/<int:pk>",
         OrderOdbFileView.as_view(),
         name="odb-file-update"),
     path("gerberOrder/<int:pk>",
         OrderGerberFileView.as_view(),
         name="gerber-file-update"),
     path("schematicsOrder/<int:pk>",
         OrderSchematicsFileView.as_view(),
         name="schemaics-file-update"),
     
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

     path("welding/",
          WeldingListAPIView.as_view(),
          name="welding-list"),
     path("welding/<uuid:uuid>/",
          WeldingDetailAPIView.as_view(),
          name="welding-details"),


     path("production/<uuid:uuid>/",
          ProductionListAPIView.as_view(),
          name="production-details"),
   
     ]

