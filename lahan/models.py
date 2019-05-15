from django.db import models

# Create your models here.
class daerah(models.Model):
    provinsi = models.CharField(max_length=20)
    def __str__(self):
        return self.provinsi
    class Meta:
        db_table = "tb_daerah"


class area(models.Model):
    provinsi = models.ForeignKey(daerah, on_delete=models.CASCADE)
    luas = models.IntegerField()
    tahun = models.IntegerField()

    class Meta:
        db_table="tb_area"