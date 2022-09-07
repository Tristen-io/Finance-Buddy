from django.urls import path, include

from .views import (
    budget_list,
    budget_detail,
    budget_update,
    budget_amount_update
    )
urlpatterns = [
    (path('list/', budget_list, name="budget-list")),
    (path('<int:budget_pk>/', budget_detail, name="budget-detail" )),
    (path('update/<int:budget_pk>/', budget_update, name='budget-update')),
    (path('update/<int:budget_pk>/amount/', budget_amount_update, name="budget-amount"))

]
