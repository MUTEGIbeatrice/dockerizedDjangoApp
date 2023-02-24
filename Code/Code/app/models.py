from django.db import models
from django.contrib.auth.models import AbstractUser
from django_cryptography.fields import encrypt


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=200,blank=True,null=True)
    


class Report(models.Model):
    STATUS_TYPE =(
        ('Open','Open'),
        ('Closed','Closed'),
    )
    SENSITIVITY_TYPE =(
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
    )
    OWNER_TYPE = (
        ('project manager1','project manager1'),
        ('project manager 2','project manager 2'),
    )
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    title = encrypt(models.CharField(max_length=200))
    description = encrypt(models.TextField(null=True,blank=True))
    
    status = models.CharField(max_length=200,choices=STATUS_TYPE)
    sensitivity_status = models.CharField(max_length=200,choices=SENSITIVITY_TYPE)
    current_owner = models.CharField(max_length=500,choices=OWNER_TYPE)
    date = models.DateField()
    
    # def save(self, *args, **kwargs):
    #      self.title = 
    #     super(Report, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
