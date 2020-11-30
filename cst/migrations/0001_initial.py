# Generated by Django 3.1.3 on 2020-11-20 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=30, verbose_name='班级名称')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='教师名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('gender', models.CharField(choices=[('boy', '男性'), ('girl', '女性')], default='boy', max_length=10, verbose_name='性别')),
                ('phone_number', models.CharField(blank=True, default=None, max_length=11, verbose_name='移动电话')),
                ('teacher_object', models.CharField(blank=True, default=None, max_length=30, verbose_name='所授课程')),
                ('teacher_worked_years', models.IntegerField(blank=True, default=None, verbose_name='任教年限')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='学生名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('gender', models.CharField(choices=[('boy', '男性'), ('girl', '女性')], default='boy', max_length=10, verbose_name='性别')),
                ('phone_number', models.CharField(blank=True, default=None, max_length=11, verbose_name='移动电话')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_class', to='cst.class')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='class_teacher',
            field=models.ManyToManyField(related_name='class_teacher', to='cst.Teacher'),
        ),
    ]