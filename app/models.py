from django.db import models

# Create your models here.


class Product_Category(models.Model):
    PCid=models.PositiveIntegerField()
    PCname=models.CharField(max_length=100)

    def __str__(self):
        return self.PCname
    

class Product(models.Model):
    PCname=models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    Pid=models.PositiveIntegerField()
    Pname=models.CharField(max_length=100)
    Pprice=models.DecimalField(max_digits=8,decimal_places=2)
    Pdescription=models.TextField()
    Pdate=models.DateField()

    def __str__(self):
        return self.Pname