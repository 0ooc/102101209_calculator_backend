from django.db import models
# Create your models here.
class Calculations(models.Model):
    arithmetic = models.CharField(max_length=1000, verbose_name='算术表达式')
    out = models.CharField(max_length=1000,verbose_name='计算结果')
    def __str__(self):
        return self.out  #将模型类以字符串的方式输出
    class Meta:
        db_table = 'Calculations'
 