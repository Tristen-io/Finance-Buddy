from django.db import models
from djmoney.models.fields import MoneyField
from User.models import AppUser


class Budget(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    goal_amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    current_amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __str__(self):
        return self.name 
# Create your models here.
