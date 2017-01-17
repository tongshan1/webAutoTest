from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Test_web(models.Model):

    STATUS = (
        ('1', 'running'),
        ('0', 'not_running'),
    )

    id = models.AutoField("测试ID", primary_key=True)
    website = models.CharField('标题', max_length=70)
    test_cases = models.CharField('测试用例', max_length=100, default="")
    # test_result = models
    test_user = models.ForeignKey('Test_user', verbose_name='测试账号')
    email = models.EmailField('报告人')
    browser = models.ForeignKey('browser', verbose_name='浏览器')

    def __str__(self):
        return self.website

    def get_absolute_url(self):
        return reverse('webEdit', kwargs={'test_id': self.pk})


class browser(models.Model):

    browser = models.CharField("浏览器", max_length=10)
    version = models.CharField("版本", max_length=10)


class Test_user(models.Model):

    user_name = models.CharField('测试账号', max_length=100)
    user_pass = models.CharField("账号密码", max_length=100)
    user_trans_pass = models.CharField("交易密码", null=True, blank=True, max_length=100)
    user_use = models.IntegerField('使用平台', default=1)
