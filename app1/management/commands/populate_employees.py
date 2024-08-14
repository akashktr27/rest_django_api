from django.core.management.base import BaseCommand
from faker import Faker
# from api.app1.models import *
from app1.models import Employee
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populate the Employee table with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(1000):
            # Create fake user
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )

            # Create fake employee
            Employee.objects.create(
                user=user,
                position=fake.job(),
                department=fake.company()
            )

        self.stdout.write(self.style.SUCCESS('Successfully added 1000 fake employees'))


