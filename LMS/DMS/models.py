from django.db import models
import datetime
# Create your models here.


class Device(models.Model):
    # 设备ID
    Device_ID = models.CharField(max_length=20)
    # 购入时间
    Input_time=models.DateField(default='')
    # 状态
    NORMAL = '正常'
    BORROWED = '借出'
    ING = '审核中'
    BANED = '报废'
    DEVICE_STATUS = (
        (NORMAL, '正常'),
        (BORROWED, '借出'),
        (ING, '审核中'),
        (BANED, '报废'),
    )
    Status=models.CharField(
        choices=DEVICE_STATUS,
        max_length=20
    )

    class Meta:
        db_table = ''
        managed = True
        verbose_name = '设备管理'
        verbose_name_plural = '设备管理'