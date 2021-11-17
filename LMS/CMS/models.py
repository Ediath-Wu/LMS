from typing import Type
from django.db import models
from django.db.models.deletion import CASCADE
from RMS.models import Receipt
# Create your models here.

class Consumable(models.Model):
    Buy_time=models.DateField('购买时间',auto_now=True)
    Receipt_ID=models.OneToOneField(to=Receipt,on_delete=CASCADE)
    Type=models.CharField('型号',max_length=20)
    Quantity=models.IntegerField('余量')
    Quantity_call=models.IntegerField('报警数量')
    
    def __str__(self) -> str:
        return Type
    
    class Meta:
        verbose_name = '耗材'
        verbose_name_plural = '耗材'