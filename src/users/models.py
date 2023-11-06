from django.db import models
from django.contrib.auth.models import AbstractUser #Custom user

# Class for custom user
class CustomUser(AbstractUser):
    
    ROLES = [
        ("O", "Operator"),
        ("C", "Custumer"),
        ("M", "Manager")
    ]
    name = models.CharField(max_length=120)
    company_role = models.CharField(max_length=1, choices=ROLES)
    

    def __str__(self):
        return f"{self.username}-{self.company_role}"