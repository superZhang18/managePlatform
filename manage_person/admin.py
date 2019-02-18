from django.contrib import admin
from .models import *

@admin.register(PersonTypeCategory)
class PersonTypeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'seq', 'u_time', ]
    # list_display_links = ['name']
    # list_editable = ['name', 'seq']
    search_fields = ['name', ]

@admin.register(PersonTypeOption)
class PersonTypeOptionAdmin(admin.ModelAdmin):
    list_display = ['person_type_category', 'name', 'seq', 'u_time']
    # list_display_links = ['name']
    # list_editable = ['name', 'seq']
    search_fields = ['person_type_category', 'name',]

@admin.register(PersonStatus)
class PersonStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'person_status_class', 'seq', 'u_time']
    # list_display_links = ['name']
    # list_editable = ['name', 'seq']
    search_fields = ['name',]

@admin.register(Address)
class Address(admin.ModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # 后台列表显示列
    # list_display = ['department', 'position', 'name', 'person_type_option']
    list_display = ['position', 'name']
    # list_display_links = ['name']
    # list_editable = ['name']
    # 后台列表查询条件
    search_fields = ['sex']
    # 后台列表通过时间查询
    list_filter = ['name']
    # radio_fields = {'department'}
