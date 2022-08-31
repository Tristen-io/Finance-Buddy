from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser


#adding the custom abstract user fields to django admin to be able to add the values. 
# class CustomUserAdmin(UserAdmin):
#     fieldsets =(
#         *UserAdmin.fieldsets,
#         (
#             'Additional Info',
#             {
#                 'fields': (
#                     'age',
#                     'nickname',
#                     'salary'
#                 )
#             }
#         )
#     )

# admin.site.register(AppUser, CustomUserAdmin)



#seletes all the the fields for UserAdmin
fields = list(UserAdmin.fieldsets)
#selects the 2nd index to be able to change the Personal Info fields to also have custom fields 
fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'age', 'nickname', 'salary')})
#loads the custom fields. 
UserAdmin.fieldsets = tuple(fields)
#registers AppUser Model using UserAdmin
admin.site.register(AppUser, UserAdmin)