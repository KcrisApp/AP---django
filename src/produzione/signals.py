from django.db.models.signals import post_save
from django.dispatch import receiver
from produzione.models import Order, Test, Smt, Verify, Welding

#If create is true i create a new istance of Smt Ict and Verify
@receiver(post_save, sender=Order)
def create_departments(sender, instance, created, **kwargs):
    print("Created departments: ",created)
    if created:
        Test.objects.create(order=instance)
        Smt.objects.create(order=instance)
        Verify.objects.create(order=instance)
        Welding.objects.create(order=instance)