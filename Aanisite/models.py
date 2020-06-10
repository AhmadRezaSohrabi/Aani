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
    

class TTMTContract(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('medicine', 'medicine'),
        ('supplement', 'supplement'),
        ('herbal_remedy', 'herbal_remedy'),
    ]
    THERAPEUTIC_CATEGORY_CHOICES = [
        ('hormonal', 'hormonal'),
        ('non_hormonal_product', 'non_hormonal_product'),
        ('non_antibiotics', 'non_antibiotics'),
        ('antibiotics', 'antibiotics'),
        ('hazardous', 'hazardous'),  
    ]
    F_AND_D_LICENSE_CHOICES = [
        ('product_license', 'product_license'),
        ('contract_manufacturing_license', 'contract_manufacturing_license'),
        ('None', None)
    ]
    generic_name = models.CharField(max_length=255, null=True, blank=True)
    trade_name = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_type = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    product_type = models.CharField(choices=PRODUCT_TYPE_CHOICES,max_length=255, null=True, blank=True)
    therapeutic_category = models.CharField(choices=THERAPEUTIC_CATEGORY_CHOICES ,max_length=255, null=True, blank=True)
    f_and_d_license = models.CharField(choices=F_AND_D_LICENSE_CHOICES, max_length=255, null=True, blank=True)
    contract_giver_representative = models.CharField(max_length=255, null=True, blank=True)
    contract_giver_authorized_person = models.CharField(max_length=255, null=True, blank=True)


class RawMaterialAndExcipientSpecifications(models.Model):
    TYPE_OF_RAW_MATERIAL_CHOICES = [
        ('powder', 'powder'),
        ('granules_ready_for_process', 'granules_ready_for_process'),
        ('pellet', 'pellet'),
    ]
    temperature_humidity_sensitive = models.BooleanField(null=True, blank=True)
    light_sensitive = models.BooleanField(null=True, blank=True)
    toxicity_substance = models.BooleanField(null=True, blank=True)
    oel_oeb_specified = models.BooleanField(null=True, blank=True)
    oel_oeb_value = models.FloatField(null=True, blank=True)
    presentation_of_valid_msds = models.BooleanField(null=True, blank=True)
    raw_material_source_country = models.CharField(max_length=255, null=True, blank=True)
    type_of_raw_material = models.CharField(choices=TYPE_OF_RAW_MATERIAL_CHOICES, max_length=255, null=True, blank=True)
    presentation_of_washing_properties = models.TextField(null=True, blank=True)