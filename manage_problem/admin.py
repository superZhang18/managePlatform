from django.contrib import admin
from .models import *
from .views import *

# =============后台全局设置=========================
# admin.site.site_header = "xxxx综合管理平台"
# admin.site.site_title = "xxxx综合管理平台"
# admin.site.index_title = "后台管理"

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_id', 'u_time', 'seq')
    list_editable = ('seq', )
    ordering = ('seq',)

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    date_hierarchy = 'inspect_date'
    list_display = ('inspect_date', 'inspect_depart', 'name_leader',
                    'name', 'type', 'context_praise', 'context_criticize', 'flag_show',
                    'colored_status')
    # list_editable = ('flag_show', )
    exclude = ('color_code',)
    list_display_links = ('inspect_date', 'inspect_depart')
    list_filter = ('inspect_depart', 'name')
    search_fields = ('inspect_date', 'inspect_depart__name', 'name_leader',
                    'name', 'context_criticize', 'context_praise')
    fieldsets = (
        ('基本信息', {
            'fields': ('inspect_date', 'inspect_depart', 'name_leader',
                       'name')
        }),
        ('检查情况', {
            'classes': ('wide', ),
            'fields': ( 'type', 'context_praise', 'context_criticize', )
        }),
        ('整改措施上报', {
            'classes': ('wide',),
            'fields': ('solution_reported_date', 'solution_reported_name',
                       'solution_reported')
        }),
        ('整改情况检查', {
            'classes': ('wide', ),
            'fields': ('status', 'context_again', 'flag_show')
        })
    )

@admin.register(ProblemChart)
class ProblemChartAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return problem_chart(request)