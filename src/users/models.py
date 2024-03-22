from django.db import models
from django.contrib.auth.models import AbstractUser #Custom user

# Class for custom user
class CustomUser(AbstractUser):
    
    ROLES = [
        ("O", "Operator"),
        ("C", "Custumer"),
        ("M", "Manager")
    ]
    DEPARTMENT = [
        ("O", "Office"),
        ("T", "Testing"),
        ("V", "Verify"),
        ("S", "SMT"),
        ("W", "Welding")
    ]
    name = models.CharField(max_length=120)
    company_role = models.CharField(max_length=1, choices=ROLES)
    department = models.CharField(max_length=1, choices=DEPARTMENT)
    

    def __str__(self):
        return f"{self.username}-{self.company_role}"