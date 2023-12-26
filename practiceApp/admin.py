from django.contrib import admin
from .models import *
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email_id','Company')
    list_filter = ('Company',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
