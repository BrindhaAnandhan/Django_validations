from django.contrib import admin
from app.models import *

# Register your models here.\

class custom(admin.ModelAdmin):
    list_display = ['Name', 'Experience', 'Mobile', 'Email', 'Portfolio']
    list_editable = ['Mobile']
    search_fields= ['Name']
    list_filter=['Name']

admin.site.register(EmployeeInfo, custom)


admin.site.site_header = 'Django_Forms'
admin.site.site_title = 'Django_Forms'
admin.site.index_title = "Forms"