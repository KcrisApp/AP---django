from django.db.models.signals import post_save
from django.dispatch import receiver
from produzione.models import Order, Test, Smt, Verify


#If create is true i create a new istance of Smt Ict and Verify
@receiver(post_save, sender=Order)
def create_profile(sender, instance, created, **kwargs):
    print("Created: ",created)
    if created:
        Test.objects.create(order=instance)
        Smt.objects.create(order=instance)
        Verify.objects.create(order=instance)