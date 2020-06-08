from django.db import models


# Create your models here.
class TheraputicCategory(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return "{}".format(self.name)
    
class Form(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return "{}".format(self.name)
    

class Product(models.Model):
    generic_name = models.CharField(max_length=63)
    trade_name = models.CharField(max_length=63)
    description = models.TextField(null=True, blank=True)
    side_effects = models.TextField(null=True, blank=True)
    dosage = models.TextField(null=True, blank=True)
    theraputic_category = models.ForeignKey(TheraputicCategory, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self):
        return "{}".format(self.trade_name)
    

