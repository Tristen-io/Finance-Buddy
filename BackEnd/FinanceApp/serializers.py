from rest_framework import serializers
from .models import Budget, Income
from User.serializers import AppUserBudgetSerializer


class BudgetSerializer(serializers.ModelSerializer):
    # user = AppUserBudgetSerializer(read_only=True)

    class Meta: 
        model = Budget
        fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
    # user = AppUserBudgetSerializer(read_only=True)

    class Meta: 
        model = Income
        fields = '__all__'