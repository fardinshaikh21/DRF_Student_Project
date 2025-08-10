from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eid', 'name', 'email')
    search_fields = ('name', 'email')

admin.site.register(Employee, EmployeeAdmin)
admin.site.site_header = "Employee Management System"    