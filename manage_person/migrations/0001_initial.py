# Generated by Django 2.1.3 on 2019-02-18 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manage_problem', '0014_auto_20190218_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='居住地点类别')),
                ('seq', models.PositiveSmallIntegerField(verbose_name='排序号')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '居住地点类别',
                'verbose_name_plural': '居住地点类别',
                'ordering': ['seq'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='姓名')),
                ('position', models.CharField(max_length=40, verbose_name='职务')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=40, verbose_name='性别')),
                ('date_birth', models.DateField(max_length=40, verbose_name='出生日期')),
                ('home', models.CharField(max_length=300, verbose_name='家庭住址')),
                ('political_status', models.CharField(choices=[('communist', '党员'), ('precommunist', '预备党员'), ('league', '团员'), ('mass', '群众')], max_length=40, verbose_name='政治面貌')),
                ('date_admit_party', models.DateField(max_length=40, verbose_name='党团时间')),
                ('military_rank', models.CharField(choices=[('107', '大校'), ('106', '上校'), ('105', '中校'), ('104', '少校'), ('103', '上尉'), ('102', '中尉'), ('101', '少尉'), ('209', '一级军士长'), ('208', '二级军士长'), ('207', '三级军士长'), ('206', '四级军士长'), ('205', '上士'), ('204', '中士'), ('203', '下士'), ('202', '上等兵'), ('201', '列兵')], max_length=40, verbose_name='军衔')),
                ('date_admit_army', models.DateField(max_length=40, verbose_name='入伍时间')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('seq', models.PositiveSmallIntegerField(verbose_name='排序号')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='address_SET', to='manage_person.Address', verbose_name='居住地点')),
                ('address_now', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='address_now_SET', to='manage_person.Address', verbose_name='现住地点')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_SET', to='manage_problem.Department', verbose_name='编制单位')),
                ('department_now', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_now_SET', to='manage_problem.Department', verbose_name='现单位')),
            ],
            options={
                'verbose_name': '人员花名册',
                'verbose_name_plural': '人员花名册',
                'ordering': ['seq', 'id'],
            },
        ),
        migrations.CreateModel(
            name='PersonStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='在位情况类别')),
                ('person_status_class', models.CharField(choices=[('in', '在位'), ('out', '不在位')], max_length=40, verbose_name='在位/不在位')),
                ('seq', models.PositiveSmallIntegerField(verbose_name='排序号')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '在位情况类别',
                'verbose_name_plural': '在位情况类别',
                'ordering': ['seq'],
            },
        ),
        migrations.CreateModel(
            name='PersonTypeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='人员区分原则')),
                ('seq', models.PositiveSmallIntegerField(verbose_name='排序号')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '人员区分原则',
                'verbose_name_plural': '人员区分原则',
                'ordering': ['seq'],
            },
        ),
        migrations.CreateModel(
            name='PersonTypeOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='人员区分选项')),
                ('seq', models.PositiveSmallIntegerField(verbose_name='排序号')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('person_type_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manage_person.PersonTypeCategory', verbose_name='人员区分原则')),
            ],
            options={
                'verbose_name': '人员区分选项',
                'verbose_name_plural': '人员区分选项',
                'ordering': ['seq'],
            },
        ),
        migrations.AddField(
            model_name='person',
            name='person_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manage_person.PersonStatus', verbose_name='在位情况'),
        ),
        migrations.AddField(
            model_name='person',
            name='person_type_option',
            field=models.ManyToManyField(to='manage_person.PersonTypeOption', verbose_name='人员区分选项'),
        ),
    ]
