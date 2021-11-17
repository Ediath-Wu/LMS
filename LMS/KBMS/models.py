from django.db import models
from django.db.models.deletion import CASCADE
from PMS.models import Person
from RMS.models import Receipt
from Tracker.models import get_fake_UUID

import random
# Create your models here.


class Kit_Board(models.Model):
    KitBoard_ID = models.CharField('开发板ID',
                                   max_length=20, default=get_fake_UUID(5))
    KitBoard_type = models.CharField('开发板型号', default='', max_length=20)
    Price = models.FloatField('价格', default=0)
    Pub_time = models.DateField('购买时间', auto_now=True)
    # 申请购买的人员
    Buyer = models.ForeignKey(Person, on_delete=models.CASCADE)
    # 对应发票信息
    Receipt_ID = models.OneToOneField(
        to=Receipt, on_delete=models.CASCADE)
    # 开发板状态
    NORMAL = '正常'
    BORROWED = '借出'
    ING = '审核中'
    BANED = '报废'
    KITBOARD_STATUS = (
        (NORMAL, '正常'),
        (BORROWED, '借出'),
        (ING, '审核中'),
        (BANED, '报废'),
    )
    Status = models.CharField(
        '开发板状态',
        choices=KITBOARD_STATUS,
        default=NORMAL,
        max_length=20
    )

    def __str__(self) -> str:
        return self.KitBoard_ID

    class Meta:
        db_table = ''
        managed = True
        verbose_name = '开发板'
        verbose_name_plural = '开发板'
