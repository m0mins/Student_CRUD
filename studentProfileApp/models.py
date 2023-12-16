from django.db import models

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = [
        ('', 'Select a gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    RELIGION_CHOICES = [
        ('', 'Select a Religion'),
        ('Islam', 'Islam'),
        ('Hindu', 'Hindu'),
        ('Buddist', 'Buddist'),
    ]
    DEPARTMENT_CHOICES = [
        ('', 'Select a Department'),
        ('CSE', 'CSE'),
        ('Civil', 'Civil'),
        ('EEE', 'EEE'),
        ('ME', 'ME'),
        ('Chemistry', 'Chemistry'),
    ]
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    su_id=models.CharField(max_length=20)
    department =models.CharField(max_length=10, choices=DEPARTMENT_CHOICES,default='')
    phone=models.CharField(max_length=15)
    age=models.PositiveIntegerField()
    image=models.ImageField(upload_to='prof_pic')
    gender =models.CharField(max_length=10, choices=GENDER_CHOICES,default='')
    religion=models.CharField(max_length=10, choices=RELIGION_CHOICES,default='')
    address=models.TextField(max_length=100)

    def __str__(self):
        return self.name

    