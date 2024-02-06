from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets

from produzione.api.permissions import IsManagerOrReadOnly


from produzione.models import Board, Order, Smt, Test, Verify, Shipping, ProductionSteps
from produzione.api.serializer import BoardSerializer, OrderSerializer, SmtSerializer, TestSerializer, VerifySerializer, BoardImagesSerializer, ShippingSerializer, ProductionStepSerializer, ProductionDetailsSerializer

# Orders views V2
class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsManagerOrReadOnly]
    lookup_field = "order_number"

#Board views V2
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsManagerOrReadOnly]
  

# Production Step views V2
class ProductionStepViewset(viewsets.ModelViewSet):
    queryset = ProductionSteps.objects.all()
    serializer_class = ProductionStepSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsManagerOrReadOnly]
    lookup_field = "uuid"
    filterset_fields = ('board', )


# Boards views
# class BoardListCreateAPIView(generics.ListCreateAPIView):

#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class BoardDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
# *************************************************************

# Orders views
# class OrderCreateAPIView(generics.CreateAPIView):

#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
#     def perform_create(self, serializer):
#         board_pk = self.kwargs.get("board_pk")
#         print(board_pk)
#         board = get_object_or_404(Board, pk=board_pk)
#         serializer.save(board=board)

# class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# class OrderListAPIView(generics.ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
# *************************************************************

class BoardImgUpdate(generics.UpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardImagesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsManagerOrReadOnly]

# Test views
class TestListAPIView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    lookup_field = "uuid"

class TestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    lookup_field = "uuid"

# class TestCreateAPIView(generics.CreateAPIView):
#     queryset = Test.objects.all()
#     serializer_class = TestSerializer

#     def perform_create(self, serializer):

#         order_pk = self.kwargs.get("order_pk")
#         print(order_pk)
#         order = get_object_or_404(Order, pk = order_pk)
#         serializer.save(order = order)

        
# *************************************************************

#Verify views
 
class VerifyListAPIView(generics.ListAPIView):

    queryset = Verify.objects.all()
    serializer_class = VerifySerializer
    lookup_field = "uuid"

class VerifyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Verify.objects.all()
    serializer_class = VerifySerializer
    lookup_field = "uuid"

# class VerifyCreateAPIView(generics.CreateAPIView):

#     queryset = Verify.objects.all()
#     serializer_class = VerifySerializer
#     lookup_field = "uuid"

#     def perform_create(self, serializer):
#         order_pk = self.kwargs.get("order_pk")
#         print(order_pk)
#         order = get_object_or_404(Order, pk = order_pk)
#         serializer.save(order = order)

# *************************************************************

# Smt views

class SmtListAPIView(generics.ListAPIView):

    queryset = Smt.objects.all()
    serializer_class = SmtSerializer
    lookup_field = "uuid"

class SmtDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Smt.objects.all()
    serializer_class = SmtSerializer
    lookup_field = "uuid"

# class SmtCreateAPIView(generics.CreateAPIView):

#     queryset = Smt.objects.all()
#     serializer_class = SmtSerializer
#     lookup_field = "uuid"

#     def perform_create(self, serializer):

#         order_pk = self.kwargs.get("order_pk")
#         print(order_pk)
#         order = get_object_or_404(Order, pk = order_pk)
#         serializer.save(order = order)

# *************************************************************
# Shipping views V2
class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "uuid"
    filterset_fields = ('order', )

# *************************************************************


# ProductionList views for caratterizzazione prodotto
class ProductionListAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = ProductionDetailsSerializer
    lookup_field = "uuid"

