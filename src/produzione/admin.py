from django.contrib import admin
from .models import Welding, Board, Order, Smt, Test, Verify, Shipping, ProductionSteps

class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_number","board", "order_quantity","shipping_date","created_at"]
    list_filter = [
         "shipping_date",
         "created_at",
         
    ]
    search_fields = (
        "order_number",
       
    )

class BoardAdmin(admin.ModelAdmin):
    list_display = ["board_name","board_code", "created_at"]
    list_filter = [
         "board_name",
         "created_at",
         
    ]
    search_fields = (
        "board_name",
        "board_code"
       
    )
class ProductionStepsAdmin(admin.ModelAdmin):
    list_display = ["step_type","step_name","created_at"]
    list_filter = [
         "step_type",
         "created_at",
         
    ]
    search_fields = (
        "step_name",
       
    )
class TestAdmin(admin.ModelAdmin):
    list_display = ["order","status","created_at"]
    list_filter = [
         "status",
         "created_at",
         
    ]
    search_fields = (
        "order",
       
    )
    
class VerifyAdmin(admin.ModelAdmin):
    list_display = ["order","status","created_at"]
    list_filter = [
         "status",
         "created_at",
         
    ]
    search_fields = (
        "order",
       
    )
class SmtAdmin(admin.ModelAdmin):
    list_display = ["order","status","created_at"]
    list_filter = [
         "status",
         "created_at",
         
    ]
    search_fields = (
        "order",
       
    )
class ShippingAdmin(admin.ModelAdmin):
    list_display = ["order","shipping_qta","shipping_date"]
    list_filter = [
         "shipping_date",
         "created_at",
         
    ]
    search_fields = (
        "order",
       
    )
class WeldingAdmin(admin.ModelAdmin):
    list_display = ["order","status","created_at"]
    list_filter = [
            "status",
            "created_at",
            
        ]
    search_fields = (
            "order",
        
        )

    
# Register your models here.
admin.site.register(Board, BoardAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Verify,VerifyAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Smt, SmtAdmin)
admin.site.register(Shipping, ShippingAdmin)
admin.site.register(ProductionSteps, ProductionStepsAdmin)
admin.site.register(Welding, WeldingAdmin)