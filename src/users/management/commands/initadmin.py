from django.core.management.base import BaseCommand, CommandError
from users.models import CustomUser
from django.conf import settings


# Admin creation comand
class Command(BaseCommand):

    def handle(self, *args, **options):
        if CustomUser.objects.count() == 0:
           
                username = settings.USERNAME
                email = settings.EMAIL
                password = settings.PASSWORD
                print('Creating account for %s (%s)' % (username, email))
                admin = CustomUser.objects.create_superuser(email=email, username=username, password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')