from django.db import models


# Create your models here.
class Cuahang(models.Model):
    ten_cua_hang = models.CharField(max_length=200)
    ma_cua_hang = models.CharField(max_length=200)
    dia_chi = models.CharField(max_length=200)
    ngay_tao = models.DateTimeField('publish date')
    
    def __str__(self):
        return self.ten_cua_hang

class san_pham(models.Model):
    ten_san_pham = models.CharField(max_length=200)
    ma_san_pham = models.CharField(max_length=200)
    
    def __str__(self):
        return self.ten_san_pham