from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from produzione.models import Order, Test, Smt, Verify, Welding, ProductionSteps, Board
import os


#ORDER SIGNALS
#***********************************************************************************#

#Signal If create is true i create a new istance of Smt Ict and Verify
@receiver(post_save, sender=Order)
def create_departments(sender, instance, created, **kwargs):
    print("Created departments: ",created)
    if created:
        Test.objects.create(order=instance)
        Smt.objects.create(order=instance)
        Verify.objects.create(order=instance)
        Welding.objects.create(order=instance)


# Signal to delete old topographic file on update order

@receiver(pre_save, sender=Order)
def auto_delete_old_file_signal(sender, instance, **kwargs):
 
    if not instance.pk:
        return False
    
    try:
        
        oldFileTopographic = Order.objects.get(pk=instance.pk).order_file_topographic
        oldFileGerber = Order.objects.get(pk=instance.pk).order_file_gerber
        oldFileOdb = Order.objects.get(pk=instance.pk).order_file_odb
        oldFileSchematics = Order.objects.get(pk=instance.pk).order_file_schematics

    except Order.DoesNotExist:
        return False

    # Delete old  file for order
    newFileTopographic = instance.order_file_topographic
    newFileGerber = instance.order_file_gerber
    newFileOdb = instance.order_file_odb
    newFileSchematics = instance.order_file_schematics
    
    
    if not oldFileTopographic == newFileTopographic and oldFileTopographic:
    
        if os.path.isfile(oldFileTopographic.path):
           
            os.remove(oldFileTopographic.path)

    if not oldFileGerber == newFileGerber and oldFileGerber:
    
        if os.path.isfile(oldFileGerber.path):
           
            os.remove(oldFileTopographic.path)

    if not oldFileOdb == newFileOdb and oldFileOdb:
    
        if os.path.isfile(oldFileOdb.path):
           
            os.remove(oldFileTopographic.path)

    if not oldFileSchematics == newFileSchematics and oldFileSchematics:
    
        if os.path.isfile(oldFileSchematics.path):
           
            os.remove(oldFileSchematics.path)
       




# Signal to delete old file top and bot when img field is update

@receiver(post_delete, sender=Order)
def auto_delete_topographic_on_delete_signal(sender, instance, **kwargs):
    

    # Delete order_filetopographic 
    if instance.order_file_topographic:

        if os.path.isfile(instance.order_file_topographic.path):
            os.remove(instance.order_file_topographic.path)

    # Delete order_filetopographic 
    if instance.order_file_schematics:

        if os.path.isfile(instance.order_file_schematics.path):
            os.remove(instance.order_file_schematics.path)
    # Delete order_filetopographic 
    if instance.order_file_odb:

        if os.path.isfile(instance.order_file_odb.path):
            os.remove(instance.order_file_odb.path)
    # Delete order_filetopographic 
    if instance.order_file_gerber:

        if os.path.isfile(instance.order_file_gerber.path):
            os.remove(instance.order_file_gerber.path)



#STEPS SIGNALS
#***********************************************************************************#

#Signal for create auto increment number order
@receiver(pre_save, sender=ProductionSteps) 
def create_step_order_number(sender, instance, **kwargs):

    if instance._state.adding:

        try:
            step = ProductionSteps.objects.all().filter(board=instance.board).reverse()[0]
        except:
            step = None

        if step:

            if step.step_order >=  1:
                instance.step_order = step.step_order +  6000
   
    else:
        print ('Instance updated!')
        pass
    

#BOARD SIGNALS
#***********************************************************************************#

# Signal to delete old img top and bot when img field is update

@receiver(pre_save, sender=Board)
def auto_delete_old_img_signal(sender, instance, **kwargs):
    
    if not instance.pk:
        return False
    
    try:
        oldImgTop = Board.objects.get(pk=instance.pk).board_img
        oldImgBot = Board.objects.get(pk=instance.pk).board_img_bot


    except Board.DoesNotExist:
        return False

    # Delete old img top
    newImgTop = instance.board_img
    if not oldImgTop == newImgTop:
    
        if os.path.isfile(oldImgTop.path):
            print('Elimino top')
            os.remove(oldImgTop.path)

    # Delete old img bot
    newImgBot = instance.board_img_bot
    if not oldImgBot == newImgBot:

        if os.path.isfile(oldImgBot.path):
            print('Elimino Bot')
            os.remove(oldImgBot.path)


# Signal to delete old img top and bot when img field is update

@receiver(post_delete, sender=Board)
def auto_delete_img_on_delete_signal(sender, instance, **kwargs):
    

    # Delete img bot
    if instance.board_img_bot:

        if os.path.isfile(instance.board_img_bot.path):
            os.remove(instance.board_img_bot.path)

    # Delete img top
    if instance.board_img:

        if os.path.isfile(instance.board_img.path):
            os.remove(instance.board_img.path)




