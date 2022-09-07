from rest_framework import serializers
from .models import Budget
from User.serializers import AppUserBudgetSerializer


class BudgetSerializer(serializers.ModelSerializer):
    # user = AppUserBudgetSerializer(read_only=True)

    class Meta: 
        model = Budget
        fields = '__all__'