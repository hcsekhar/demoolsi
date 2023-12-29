from django.db import models

# Create your models here.
class product_DB(models.Model):
    product_Image = models.ImageField(upload_to='images', null=True)
    product_Title = models.CharField(max_length=1000)
    product_price = models.IntegerField(max_length=6)
    product_Description = models.CharField(max_length=10000)
    product_Usage = models.CharField(max_length=10000)
    product_Features = models.CharField(max_length=10000)
    product_Benefits = models.CharField(max_length=10000)
    
