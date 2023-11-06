from email.policy import default
import re
from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models

from core.models import TimeStampedModel
import uuid as uuid_lib

# Board model.
class Board(TimeStampedModel):

    uuid = models.UUIDField(default=uuid_lib.uuid4 ,editable=False)
    customer = models.CharField(max_length=180, default="")
    board_name = models.CharField(max_length=180)
    board_code = models.CharField(max_length=180)
    board_rev = models.CharField(max_length=30)
    board_img = models.ImageField(upload_to="img", default='img/no-image.jpg')
    board_file = models.FileField(null=True, blank=True)
    

    def __str__(self):
        return self.board_name
    
    class Meta:

        verbose_name = "Board"
        verbose_name_plural = "Boards"
    
# Order model 

class Order(TimeStampedModel):

    uuid = models.UUIDField(default=uuid_lib.uuid4 ,editable=False)

    order_number = models.CharField(max_length=120, unique=True)
    order_quantity = models.PositiveBigIntegerField()
    order_process_note = models.TextField(blank=True, null=True)
    order_serialnumber = models. CharField(max_length=120, blank=True, null=True)
    

    board = models.ForeignKey(Board, on_delete= models.CASCADE, related_name="order")

    def __str__(self):
        return self.order_number
    
    class Meta:

        verbose_name = "Order"
        verbose_name_plural = "Orders"

# TODO: da implementare modello spedizione 
class Test(TimeStampedModel):

    uuid = models.UUIDField(default=uuid_lib.uuid4 ,editable=False)

    ict = models.BooleanField(default=False, null=True)
    aoi = models.BooleanField(default=False, null=True)
    xray = models.BooleanField(default=False, null=True)
    functional = models.BooleanField(default=False, null=True)
    non_compliance = models.CharField(max_length=120, null=True)
    missing_component = models.CharField(max_length=120, null=True)
    serialnumber = models.CharField(max_length=120, null=True)
    note = models.CharField(max_length=120, null=True)
    status = models.BooleanField(default=False, null=True)
    # create_new = models.BooleanField(default=False)
   
    order = models.OneToOneField(Order,on_delete= models.CASCADE, related_name="order_test")

    def __str__(self):
        return self.order.order_number
    
    class Meta:

        verbose_name = "Test"
        verbose_name_plural = "Tests"

class Verify(TimeStampedModel):

    uuid = models.UUIDField(default=uuid_lib.uuid4 ,editable=False)

    missing_component = models.CharField(max_length=120, null=True)
    manual_work = models.CharField(max_length=120, null=True)
    changes_after_testing = models.CharField(max_length=120, null=True)
    verify_date_create = models.DateTimeField(auto_now_add=True, null=True)
    create_new = models.BooleanField(default=False, null=True)
    status = models.BooleanField(default=False, null=True)
    order = models.OneToOneField(Order,on_delete= models.CASCADE, related_name="order_verify")

    def __str__(self):
        return "%s %s" % (self.order, self.verify_date_create)
    
    class Meta:

        verbose_name = "Verify"
        verbose_name_plural = "Verify"

class Smt(TimeStampedModel):

    uuid = models.UUIDField(default=uuid_lib.uuid4 ,editable=False)
    
    oven_top = models.CharField(max_length=120, null=True)
    oven_bot = models.CharField(max_length=120, null=True)
    cream_type = models.CharField(max_length=120, null=True)
    mydata_program = models.CharField(max_length=120, null=True)
    recast_profile_top = models.CharField(max_length=120, null=True)
    recast_profile_bot = models.CharField(max_length=120, null=True)
    my500_top = models.CharField(max_length=120, null=True)
    my500_bot = models.CharField(max_length=120, null=True)
    screen_printer_top = models.CharField(max_length=120, null=True)
    screen_printer_bot = models.CharField(max_length=120, null=True)
    cream_test = models.BooleanField(default=False, null=True)
    note = models.CharField(max_length=120, null=True)
    missing_component = models.CharField(max_length=120, null=True)
    status = models.BooleanField(default=False, null=True)

    fridge_temperature = models.BooleanField(default=False, null=True)
    cream_expiration = models.BooleanField(default=False, null=True)
    frame_status = models.BooleanField(default=False, null=True)
    cream_deposit = models.BooleanField(default=False, null=True)
    pick_and_place_setup = models.BooleanField(default=False, null=True)
    board_check = models.BooleanField(default=False, null=True)
    oven_parameters = models.BooleanField(default=False, null=True)
    check_status = models.BooleanField(default=False, null=True)
    create_new = models.BooleanField(default=False, null=True)
   
    order = models.OneToOneField(Order,on_delete= models.CASCADE, related_name="order_smt")

    def __str__(self):
        return "%s %s" % (self.order, self.smt_date_create)
    
    class Meta:

        verbose_name = "Smt"
        verbose_name_plural = "Smt"

class Shipping(TimeStampedModel):

    uuid = models.UUIDField(default=uuid_lib.uuid4 ,editable=False)

    shipping_qta = models.PositiveIntegerField()
    shipping_check = models.BooleanField(default=False)
    shipping_date = models.DateTimeField(null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_shipping")

    class Meta:

        verbose_name = "Shipping"
        verbose_name_plural = "Shippings"