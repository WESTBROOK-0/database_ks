from django.db import models

# Create your models here.
class Chubanshe(models.Model):
    cbs_id=models.IntegerField(primary_key=True,verbose_name='出版社号')
    cbs_name=models.CharField(max_length=20,verbose_name='出版社名')
    cbs_kucun=models.IntegerField(null=True,verbose_name='库存量')

    def __str__(self):
        return self.cbs_name

    class Meta:
        verbose_name_plural = '出版社表'
        verbose_name = '出版社表'

class Jiaocai(models.Model):
    jc_id=models.CharField(max_length=30,primary_key=True,verbose_name='教材号')
    jc_name=models.CharField(max_length=20,verbose_name='教材名')
    cbs_name = models.CharField(max_length=20, verbose_name='出版社名',null=True)
    zuozhe=models.CharField(max_length=20,verbose_name='作者')
    danjia=models.IntegerField(verbose_name='单价')
    chubanshe=models.ManyToManyField(Chubanshe)

    def __str__(self):
        return self.jc_name

    class Meta:
        verbose_name_plural = '教材表'
        verbose_name = '教材表'

class Dinggou(models.Model):
    jc_id = models.CharField(max_length=30,primary_key=True, verbose_name='教材号')
    cbs_id = models.IntegerField(verbose_name='出版社号')
    xx_id = models.IntegerField(verbose_name='学校号')
    dg_dgliang=models.IntegerField(verbose_name='订购量')
    dg_dhliang=models.IntegerField(null=True,verbose_name='到货量')
    dg_lyliang=models.IntegerField(null=True,verbose_name='领用量')
    chubanshe=models.ManyToManyField(Chubanshe)

    def __str__(self):
        return str(self.dg_dgliang)

    class Meta:
        verbose_name_plural = '订购表'
        verbose_name = '订购表'

class Xuexiao(models.Model):
    xx_id=models.IntegerField(primary_key=True,verbose_name='学校号')
    xx_name=models.CharField(max_length=20,verbose_name='学校名')
    chubanshe=models.ManyToManyField(Chubanshe)
    dinggou=models.OneToOneField(Dinggou,on_delete=models.CASCADE)

    def __str__(self):
        return self.xx_name

    class Meta:
        verbose_name_plural = '学校表'
        verbose_name = '学校表'


