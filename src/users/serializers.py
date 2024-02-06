from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = CustomUser
        exclude = ["id", "password","user_permissions","is_active", 'is_superuser','is_staff','groups']
    
    # def get_created_at(self, instance):
    #     return instance.created_at.strftime("%d/%m/%Y")