# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='browser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser', models.CharField(max_length=10, verbose_name='浏览器')),
                ('version', models.CharField(max_length=10, verbose_name='版本')),
            ],
        ),
        migrations.CreateModel(
            name='Test_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='测试账号')),
                ('user_pass', models.CharField(max_length=100, verbose_name='账号密码')),
                ('user_trans_pass', models.CharField(blank=True, max_length=100, null=True, verbose_name='交易密码')),
                ('user_use', models.IntegerField(default=1, verbose_name='使用平台')),
            ],
        ),
        migrations.CreateModel(
            name='Test_web',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='测试ID')),
                ('website', models.CharField(max_length=70, verbose_name='标题')),
                ('test_cases', models.CharField(default='', max_length=100, verbose_name='测试用例')),
                ('email', models.EmailField(max_length=254, verbose_name='报告人')),
                ('browser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AutoTest_project.browser', verbose_name='浏览器')),
                ('test_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AutoTest_project.Test_user', verbose_name='测试账号')),
            ],
        ),
    ]
