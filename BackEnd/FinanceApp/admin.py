from ast import In
from django.contrib import admin
from .models import Budget, Income
# Register your models here.

admin.site.register(Budget)
admin.site.register(Income)