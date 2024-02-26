from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from produzione.models import Order, Test, Smt, Verify, Welding, ProductionSteps

#If create is true i create a new istance of Smt Ict and Verify
@receiver(post_save, sender=Order)
def create_departments(sender, instance, created, **kwargs):
    print("Created departments: ",created)
    if created:
        Test.objects.create(order=instance)
        Smt.objects.create(order=instance)
        Verify.objects.create(order=instance)
        Welding.objects.create(order=instance)

# @receiver(pre_init, sender=ProductionSteps)   
# def create_step_number(instance, **kwargs):

#     previous = ProductionSteps.objects.all().order_by('-step_number')[0].step_number
#     print(f'Instance: {previous}')
#     instance.save()
#     return instance
@receiver(pre_save, sender=ProductionSteps) 
def create_step_order_number(sender, instance, **kwargs):

    if instance._state.adding:
        print ('Instance created!')


        try:
            step = ProductionSteps.objects.all().filter(board=instance.board).reverse()[0]
        except:
            step = None

        if step:
            print("sono qui")
            if step.step_order >=  1:
                instance.step_order = step.step_order +  6000
   
    else:
        print ('Instance updated!')
        pass
    
