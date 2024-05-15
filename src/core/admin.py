from django.contrib import admin
from .models import DataLog

class DataLogAdmin(admin.ModelAdmin):
    list_display = ["action", "http_request_methods","created_at"]
    list_filter = [
         "http_request_methods",
         "operation_type",
         "created_at"
    ]
    search_fields = (
        "message",
       
    )

# Register your models here.
admin.site.register(DataLog, DataLogAdmin)
