from django.db import models
from django.utils.html import format_html

#单位表
class Department(models.Model):
    name = models.CharField(max_length=40, verbose_name='单位名称')
    level = models.CharField(max_length=40, blank=True, null=True, verbose_name='单位级别')
    parent_id = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='上级单位')
    seq = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='排序号')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    u_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    class Meta:
        verbose_name = '单位列表'
        verbose_name_plural = '单位列表'
        ordering = ['seq']
    def __str__(self):
        if self.parent_id is None:
            return '{}'.format(self.name)
        else:
            return '{}{}'.format(self.parent_id, self.name)

#问题情况汇总表
class Problem(models.Model):
    Status = (
        ('已整改', '已整改'),
        ('已采取措施', '已采取措施'),
        ('未整改', '未整改'),
        ('待查', '待查'),
    )
    Type = (
        ('good', '好的方面'),
        ('bad', '存在问题'),
    )
    inspect_date = models.DateField(auto_now=False, verbose_name='检查时间')
    inspect_depart = models.ForeignKey('Department', on_delete= models.PROTECT, verbose_name='受检单位')
    name_leader = models.CharField(max_length=60, verbose_name='带队领导')
    name = models.CharField(max_length=60, verbose_name='检查人')

    type = models.CharField(max_length=20, default='', choices=Type, verbose_name='类别')
    context_praise = models.TextField(verbose_name='好的方面')
    context_criticize = models.TextField(verbose_name='存在不足')

    solution_reported_date = models.DateField(auto_now=False, null=True, blank=True, verbose_name='整改措施上报时间')
    solution_reported_name = models.CharField(max_length=60, blank=True, verbose_name='上报人')
    solution_reported = models.TextField(default='暂无', verbose_name='责任单位上报整改措施')

    status = models.CharField(max_length=40, choices=Status, default='未整改', verbose_name='是否整改')
    context_again = models.TextField(default='无', verbose_name='回头看情况')

    flag_show = models.BooleanField(verbose_name='是否显示')

    c_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    u_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    color_code = models.CharField(max_length=20, default='', blank=True)
    class Meta:
        verbose_name = '检查情况登记表'
        verbose_name_plural = verbose_name
        ordering = ['inspect_date']
    def colored_status(self):
        if self.status == '未整改':
            color_code = 'red'
        elif self.status == '待查':
            color_code = 'black'
        else:
            color_code = 'green'
        return format_html(
            '<span style="color:{};">{}</span>',
            color_code,
            self.status,
        )
    colored_status.short_description = u'整改情况'
    def __str__(self):
        # return '{0}{1}'.format(self.inspect_time, self.inspect_depart)
        return self.name

#问题汇总展示图表
class ProblemChart(models.Model):
    class Meta:
        verbose_name = '问题汇总展示图表'
        verbose_name_plural = verbose_name