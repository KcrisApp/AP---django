from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import  CustomUserChangeForm, CustomUserForm

from .models import CustomUser
# Register your models here.

# Custom user
class CustomUserAdmin(UserAdmin):

    
    form = CustomUserChangeForm
    
    model = CustomUser
    list_display  =  ("username" ,"name", "company_role")
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'company_role',
                    'name'
                ),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)