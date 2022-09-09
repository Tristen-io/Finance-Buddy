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


payment_schedule_choices = (
        ("monthly", "monthly"), 
        ("semi-monthly", "semi-monthly"), 
        ("bi-weekly", "bi-weekly"), 
        ("weekly", "weekly"),
        ("one-time", "one-time"),
        )
income_type_choices = (
    ("salary", "salary"),
    ("property", "property"),
    ("business", "business"),
    ("other", "other")
)

class Income(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    payment_schedule = models.CharField(
        max_length=20,
        choices= payment_schedule_choices,
    )
    type = models.CharField(
        max_length=20,
        choices = income_type_choices
    )


    
