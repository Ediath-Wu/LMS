from django.db import models

# Create your models here.


class Receipt(models.Model):
    Num_receipt = models.CharField('发票号', max_length=100)
    get_date=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '发票'
        verbose_name_plural = '发票'

    def __str__(self) -> str:
        return str(self.Num_receipt)
