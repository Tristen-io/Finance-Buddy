import json
from shutil import ReadError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Budget
from User.models import AppUser
from djmoney.money import Money

from .serializers import (
    BudgetSerializer
)
# Create your views here.


@api_view(['GET', 'POST'])
def budget_list(request):
    if request.method == 'GET':
        try:
            budgets = Budget.objects.all()
        except:
            return Response({"message": "could not get budgets"})
        serialized = BudgetSerializer(budgets, many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        content = json.loads(request.body)
        try:
            user = AppUser.objects.get(id=content['user'])
            content['user'] = user
        except:
            return Response({"message": "user does not exist"})
        try:
            budget = Budget.objects.create(**content)
            serialized = BudgetSerializer(budget)
            return Response(serialized.data)
        except:
            return Response({"message": "creation of budget went wrong"})


@api_view(['GET'])
def budget_detail(request, budget_pk):
    if request.method == "GET":
        try:
            budget = Budget.objects.get(pk=budget_pk)
        except:
            return Response({"message": "could not find budget object by the given pk"})
        serialized = BudgetSerializer(budget)
        return Response(serialized.data)

@api_view(['PUT'])
def budget_update(request, budget_pk):
    if request.method == 'PUT':
        content = json.loads(request.body)
        try:
            budget = Budget.objects.filter(pk=budget_pk).update(**content)
            updated_budget = Budget.objects.get(pk=budget_pk)
        except:
            return Response({"message": "budget not found by pk"})
        serialized = BudgetSerializer(updated_budget)
        return Response(serialized.data)

@api_view(['PUT'])
def budget_amount_update(request, budget_pk):
    content = json.loads(request.body)
    try:
        budget = Budget.objects.get(pk=budget_pk)
    except:
        return Response({"message": "could not get budget instance with PK"})
    try:
        new_total = budget.current_amount + Money(content['amount'], 'USD')
    except:
        return Response({"message": "could not add the current amount to new amount"})
    if new_total < Money(0, 'USD'):
        updated_content = {"current_amount": 0}
        try:
            Budget.objects.filter(pk=budget_pk).update(**updated_content)
            updated_budget = Budget.objects.get(pk=budget_pk)
            serialized = BudgetSerializer(updated_budget)
        except:
            return Response({"message": "could not find budget object or update with content from request"})

        return Response(serialized.data)
    else:
        updated_content = {"current_amount": new_total}
        try:
            Budget.objects.filter(pk=budget_pk).update(**updated_content)
            updated_budget = Budget.objects.get(pk=budget_pk)
            serialized = BudgetSerializer(updated_budget)
        except:
            return Response({"message": "could not find budget object or update with content from request"})

        return Response(serialized.data)


    
    
