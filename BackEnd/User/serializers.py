from rest_framework import serializers
from .models import AppUser

# this is only for the budget serializer to get the ID of the user
class AppUserBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id']