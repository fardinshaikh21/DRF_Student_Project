from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')
    search_fields = ('name', 'email')   


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.site_header = "Student Management Admin"