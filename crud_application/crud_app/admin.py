from django.contrib import admin
from crud_app.models import UserTable

class UserTableAdmin(admin.ModelAdmin):                       #u need to know
    list_display=["emp_name","emp_id"]

admin.site.register(UserTable,UserTableAdmin) 