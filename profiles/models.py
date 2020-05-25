from django.db import models
from django.contrib.auth.models import User

GROUP_TYPES = ('patient', 'doctor', 'receptionist', 'lab_attendant', 'hr_manager', 'inventory_manager')
# Added code in 0002_auto_20200524_1632.py file in migrations folder to automatically generate groups.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
)
# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    contact_no = models.IntegerField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    dob = models.DateField(blank=True, null=True)
    blood_group = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')      
    contact_no = models.IntegerField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    blood_group = models.CharField(max_length=3, null=True)
    age = models.IntegerField(null=True)
    Outstanding = models.IntegerField(null=True)
    paid = models.IntegerField(null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username