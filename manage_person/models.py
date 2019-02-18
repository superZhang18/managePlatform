from django.db import models

#人员区分原则表
class PersonTypeCategory(models.Model):
    name = models.CharField(max_length=60, verbose_name='人员区分原则')  # 人员区分原则，比如专业、居住地点、在位情况等等
    seq = models.PositiveSmallIntegerField(verbose_name='排序号')  # 排序号
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')  # 添加时间
    u_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')  # 更新时间
    class Meta:
        verbose_name = '人员区分原则'
        verbose_name_plural = '人员区分原则'
        ordering = ['seq']
    def __str__(self):
        return self.name

#人员区分原则的选项表
class PersonTypeOption(models.Model):
    person_type_category = models.ForeignKey('PersonTypeCategory', on_delete=models.PROTECT, verbose_name='人员区分原则') #依赖人员区分原则表
    name = models.CharField(max_length=60, verbose_name='人员区分选项')  # 人员区分选项
    seq = models.PositiveSmallIntegerField(verbose_name='排序号')  # 排序号
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')  # 添加时间
    u_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')  # 更新时间
    class Meta:
        verbose_name = '人员区分选项'
        verbose_name_plural = '人员区分选项'
        ordering = ['seq']
    def __str__(self):
        return self.name

#人员在位情况分类表
class PersonStatus(models.Model):
    StatusClass = (
        ('in', '在位'),
        ('out', '不在位'),
    )
    name = models.CharField(max_length=60, verbose_name='在位情况类别')
    person_status_class = models.CharField(max_length=40, choices=StatusClass, verbose_name='在位/不在位')
    seq = models.PositiveSmallIntegerField(verbose_name='排序号')  # 排序号
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')  # 添加时间
    u_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')  # 更新时间
    class Meta:
        verbose_name = '在位情况类别'
        verbose_name_plural = '在位情况类别'
        ordering = ['seq']
    def __str__(self):
        return self.name

#居住地点分类表
class Address(models.Model):
    name = models.CharField(max_length=60, verbose_name='居住地点类别')
    seq = models.PositiveSmallIntegerField(verbose_name='排序号')  # 排序号
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')  # 添加时间
    u_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')  # 更新时间
    class Meta:
        verbose_name = '居住地点类别'
        verbose_name_plural = '居住地点类别'
        ordering = ['seq']
    def __str__(self):
        return self.name

#人员花名册表
class Person(models.Model):
    Gender = (
        ('male', '男'),
        ('female', '女'),
    )
    PoliticalStatus = (
        ('communist', '党员'),
        ('precommunist', '预备党员'),
        ('league', '团员'),
        ('mass', '群众'),
    )
    MilitaryRank = (
        ('107', '大校'),
        ('106', '上校'),
        ('105', '中校'),
        ('104', '少校'),
        ('103', '上尉'),
        ('102', '中尉'),
        ('101', '少尉'),
        ('209', '一级军士长'),
        ('208', '二级军士长'),
        ('207', '三级军士长'),
        ('206', '四级军士长'),
        ('205', '上士'),
        ('204', '中士'),
        ('203', '下士'),
        ('202', '上等兵'),
        ('201', '列兵'),
    )
    department = models.ForeignKey('manage_problem.Department', related_name='department_SET', on_delete=models.PROTECT, verbose_name='编制单位')  # 编制单位
    department_now = models.ForeignKey('manage_problem.Department', related_name='department_now_SET', on_delete=models.PROTECT, verbose_name='现单位')  # 现工作单位
    name = models.CharField(max_length=40, verbose_name='姓名') #姓名
    position = models.CharField(max_length=40, verbose_name='职务') #职务
    person_status = models.ForeignKey('PersonStatus', on_delete=models.PROTECT, verbose_name='在位情况')  # 在位情况
    address = models.ForeignKey('Address', related_name='address_SET', on_delete=models.PROTECT, verbose_name='居住地点')  # 居住地点
    address_now = models.ForeignKey('Address', related_name='address_now_SET', on_delete=models.PROTECT, verbose_name='现住地点')  # 现住地点
    person_type_option = models.ManyToManyField('PersonTypeOption', verbose_name='人员区分选项')  # 人员类别区分，多选，依靠人员区分原则的选项表
    sex = models.CharField(max_length=40, choices=Gender, default='男', verbose_name='性别') #性别
    date_birth = models.DateField(max_length=40, verbose_name='出生日期') #出生日期
    home = models.CharField(max_length=300, verbose_name='家庭住址') #家庭住址
    political_status = models.CharField(max_length=40, choices=PoliticalStatus, verbose_name='政治面貌') #政治面貌
    date_admit_party = models.DateField(max_length=40, verbose_name='党团时间') #入党日期
    military_rank = models.CharField(max_length=40, choices=MilitaryRank, verbose_name='军衔') #军衔
    date_admit_army = models.DateField(max_length=40, verbose_name='入伍时间') #入伍时间
    remarks = models.TextField(verbose_name='备注', blank=True)
    seq = models.PositiveSmallIntegerField(verbose_name='排序号')  # 排序号
    class Meta:
        verbose_name = '人员花名册'
        verbose_name_plural = '人员花名册'
        ordering = ['seq', 'id']
