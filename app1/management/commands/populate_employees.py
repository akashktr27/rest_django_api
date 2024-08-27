from django.core.management.base import BaseCommand
from faker import Faker
# from api.app1.models import *
from app1.models import Employee
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populate the Employee table with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        i = 0
        for _ in range(100000):
            # Create fake user
            print('i', i)


            # Create fake employee
            Employee.objects.create(
                name=fake.name,
                position=fake.job(),
                department=fake.company()
            )
            i += 1
        self.stdout.write(self.style.SUCCESS('Successfully added 100000 fake employees'))


