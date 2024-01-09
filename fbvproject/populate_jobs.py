import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'fbvproject.settings')
import django
django.setup()


from testApp.models import *
from faker import Faker
from random import *
fake = Faker()

def populate(n):
    for i in range(n):
        feno = randrange(1001,9999)
        fename = fake.name()
        fesal = randrange(30000,50000)
        feaddr = fake.city()

        employee_record = Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)

populate(20)
