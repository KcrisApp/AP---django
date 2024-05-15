from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from produzione.models import Order, Test, Smt, Verify,Shipping, Welding, ProductionSteps, Board
from .models import DataLog
import os


#STEPS SIGNALS
#***********************************************************************************#

#Signal for step log
@receiver(post_save, sender=ProductionSteps) 
def log_step_create_update(sender, instance, created,  **kwargs):

    if created:
        message = f"Created {instance.step_name} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="POST",operation_type='Step', action="created step", message=message)        
        log.save()
        
    else:
        
        message = f"Update {instance.step_name} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="PATCH",operation_type='Step', action="update step", message=message)        
        log.save()


@receiver(pre_delete, sender=ProductionSteps) 
def log_step_delete(sender, instance,  **kwargs):

        message = f"Delete {instance.step_name} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="DELETE",operation_type='Step',action="delete step", message=message)        
        log.save()

#***********************************************************************************#
   

#Order SIGNALS
#***********************************************************************************#

#Signal for step log
@receiver(post_save, sender=Order) 
def log_order_create_update(sender, instance, created,  **kwargs):

    if created:
        message = f"Created {instance.order_number} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="POST",operation_type="Order", action="created order", message=message)        
        log.save()
        
    else:
        message = f"Update {instance.order_number} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="PATCH",operation_type="Order", action="update order", message=message)        
        log.save()


@receiver(pre_delete, sender=Order) 
def log_order_delete(sender, instance,  **kwargs):

        message = f"Delete {instance.order_number} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="DELETE",operation_type="Order", action="delete order", message=message)        
        log.save()

#***********************************************************************************#
   
#Board SIGNALS
#***********************************************************************************#

#Signal for Board log
@receiver(post_save, sender=Board) 
def log_board_create_update(sender, instance, created,  **kwargs):

    if created:
        message = f"Created {instance.board_name} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="POST",operation_type="Board",action="created board", message=message)        
        log.save()
        
    else:
        message = f"Update {instance.board_name} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="PATCH",operation_type="Board", action="update board", message=message)        
        log.save()


@receiver(pre_delete, sender=Board) 
def log_board_delete(sender, instance,  **kwargs):

        message = f"Delete {instance.board_name} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="DELETE",operation_type="Board", action="delete board", message=message)        
        log.save()

#***********************************************************************************#

#Test SIGNALS
#***********************************************************************************#

#Signal for Board log
@receiver(post_save, sender=Test) 
def log_test_create_update(sender, instance, created,  **kwargs):

    if created:
        message = f"Created test uuid: {instance.uuid}"
        log = DataLog(http_request_methods="POST",operation_type="Test",action="created board", message=message)        
        log.save()
        
    else:
        message = f"Update test: {instance.firma} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="PATCH",operation_type="Test", action="update board", message=message)        
        log.save()


@receiver(pre_delete, sender=Test) 
def log_test_delete(sender, instance,  **kwargs):

        message = f"Delete test: {instance.firma} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="DELETE",operation_type="Test", action="delete board", message=message)        
        log.save()

#***********************************************************************************#


#Verify SIGNALS
#***********************************************************************************#

#Signal for Board log
@receiver(post_save, sender=Verify) 
def log_verify_create_update(sender, instance, created,  **kwargs):

    if created:
        message = f"Created verify uuid: {instance.uuid}"
        log = DataLog(http_request_methods="POST",operation_type="Verify",action="created verify", message=message)        
        log.save()
        
    else:
        message = f"Update verify: {instance.firma} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="PATCH",operation_type="Verify", action="update verify", message=message)        
        log.save()


@receiver(pre_delete, sender=Verify) 
def log_verify_delete(sender, instance,  **kwargs):

        message = f"Delete verify: {instance.firma} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="DELETE",operation_type="Verify", action="delete verify", message=message)        
        log.save()

#***********************************************************************************#
  
#Smt SIGNALS
#***********************************************************************************#

#Signal for Board log
@receiver(post_save, sender=Smt) 
def log_smt_create_update(sender, instance, created,  **kwargs):

    if created:
        message = f"Created smt uuid: {instance.uuid}"
        log = DataLog(http_request_methods="POST",operation_type="Smt",action="created smt", message=message)        
        log.save()
        
    else:
        message = f"Update smt: {instance.firma} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="PATCH",operation_type="Smt", action="update smt", message=message)        
        log.save()


@receiver(pre_delete, sender=Smt) 
def log_smt_delete(sender, instance,  **kwargs):

        message = f"Delete smt: {instance.firma} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="DELETE",operation_type="Smt", action="delete smt", message=message)        
        log.save()

#***********************************************************************************#
  
#Welding SIGNALS
#***********************************************************************************#

#Signal for Board log
@receiver(post_save, sender=Welding) 
def log_welding_create_update(sender, instance, created,  **kwargs):

    if created:
        message = f"Created welding uuid: {instance.uuid}"
        log = DataLog(http_request_methods="POST",operation_type="Welding",action="welding smt", message=message)        
        log.save()
        
    else:
        message = f"Update welding: {instance.firma} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="PATCH",operation_type="Welding", action="welding smt", message=message)        
        log.save()


@receiver(pre_delete, sender=Welding) 
def log_welding_delete(sender, instance,  **kwargs):

        message = f"Delete welding: {instance.firma} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="DELETE",operation_type="Welding", action="welding smt", message=message)        
        log.save()

#***********************************************************************************#


#Shipping SIGNALS
#***********************************************************************************#

#Signal for Board log
@receiver(post_save, sender=Shipping) 
def log_shipping_create_update(sender, instance, created,  **kwargs):

    if created:
        message = f"Created shipping uuid: {instance.uuid}"
        log = DataLog(http_request_methods="POST",operation_type="Shipping",action="shipping smt", message=message)        
        log.save()
        
    else:
        message = f"Update shipping: {instance.firma} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="PATCH",operation_type="Shipping", action="shipping smt", message=message)        
        log.save()


@receiver(pre_delete, sender=Shipping) 
def log_shipping_delete(sender, instance,  **kwargs):

        message = f"Delete shipping: {instance.firma} uuid: {instance.uuid}"
        log = DataLog(http_request_methods="DELETE",operation_type="Shipping", action="shipping smt", message=message)        
        log.save()

#***********************************************************************************#
  