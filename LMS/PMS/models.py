from django.db import models
from Tracker.models import get_fake_UUID
# Create your models here.


class Person(models.Model):
    first_name = models.CharField('姓', max_length=20)
    last_name = models.CharField('名', max_length=20)
    mail = models.CharField('邮箱', max_length=20, default='')
    peopleID = models.CharField('ID', max_length=20, default=get_fake_UUID(5))
    # 人员权限
    ADMIN = '管理员'
    SITEADMIN = '网站管理员'
    SUPERADMIN = '超级管理员'
    USER = '骨干成员'
    OTHER = '普通人员'
    GUEST = '访客'
    BACKLIST = '黑名单'
    AUTHORIZATION = (
        (ADMIN, '管理员'),
        (SITEADMIN, '网站管理员'),
        (SUPERADMIN, '超级管理员'),
        (USER, '骨干成员'),
        (OTHER, '普通人员'),
        (GUEST, '访客'),
        (BACKLIST, '黑名单')
    )
    Authorizate = models.CharField(
        max_length=16,
        choices=AUTHORIZATION,
        default=USER
    )

    def __str__(self) -> str:
        return self.first_name+self.last_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = '人员'
        verbose_name_plural = '人员'


# 模类PMS.models.Person不声明明确的应用程序标签，也不在已安装应用程序的应用程序中。
