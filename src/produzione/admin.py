from django.contrib import admin
from .models import Board, Order, Smt, Test, Verify, Shipping

# Register your models here.
admin.site.register(Board)
admin.site.register(Order)
admin.site.register(Verify)
admin.site.register(Test)
admin.site.register(Smt)
admin.site.register(Shipping)