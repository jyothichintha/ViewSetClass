from django.db import models

# Create your models here.
class Product_Catagory(models.Model):
    Pcid=models.IntegerField(primary_key=True)
    PcName=models.CharField(max_length=100)

    def __str__(self):
        return self.PcName


class Product(models.Model):
    Pcname=models.ForeignKey(Product_Catagory,on_delete=models.CASCADE)
    Pid=models.PositiveIntegerField()
    Pname=models.CharField(max_length=100)
    Price=models.DecimalField(max_digits=6,decimal_places=2)
    date=models.DateField()

    def __str__(self):
        return self.Pname




