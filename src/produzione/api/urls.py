from django.urls import path, include
# from produzione.api.views import OrderViewset,BoardViewSet, BoardListCreateAPIView, BoardDetailAPIView, OrderCreateAPIView, OrderDetailAPIView, OrderListAPIView, SmtCreateAPIView, SmtDetailAPIView, SmtListAPIView, TestCreateAPIView, TestDetailAPIView, TestListAPIView, VerifyCreateAPIView, VerifyDetailAPIView, VerifyListAPIView
from produzione.api.views import BoardImgUpdate, OrderViewset,BoardViewSet, TestListAPIView, TestDetailAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"order",OrderViewset)
router.register(r"board",BoardViewSet)



urlpatterns = [
     path("",include(router.urls)),
     # path("board/",
     #     BoardListCreateAPIView.as_view(),
     #     name="board-list"),

     # path("board/<int:pk>/",
     #     BoardDetailAPIView.as_view(),
     #     name="board-detail"),

     # path("board/<int:board_pk>/order/",
     #     OrderCreateAPIView.as_view(),
     #     name="order-board"),

     # path("order/<int:pk>/",
     #     OrderDetailAPIView.as_view(),
     #     name="order-detail"),

     # path("order/",
     #     OrderListAPIView.as_view(),
     #     name="order-list"),
     path("boardImgUpdate/<int:pk>",
         BoardImgUpdate.as_view(),
         name="board-img-update"),
     path("test/",
         TestListAPIView.as_view(),
         name="test-list"),

     path("test/<int:pk>/", 
          TestDetailAPIView.as_view(),
          name="test-details"),

     # path("order/<int:order_pk>/test",
     #      TestCreateAPIView.as_view(),
     #      name="test-create"),

     # path("verify/",
     #      VerifyListAPIView.as_view(),
     #      name="verify-list"),

     # path("verify/<int:pk>/",
     #      VerifyDetailAPIView.as_view(),
     #      name="verify-details"),

     # path("order/<int:order_pk>/verify", 
     #      VerifyCreateAPIView.as_view(), 
     #      name="verify-create"),

     # path("smt/",
     #      SmtListAPIView.as_view(),
     #      name="smt-list"),

     # path("smt/<int:pk/",
     #      SmtDetailAPIView.as_view(),
     #      name="smt-details"),

     # path("order/<int:order_pk>/smt", 
     #      SmtCreateAPIView.as_view(), 
     #      name="smt-create"),
     ]

