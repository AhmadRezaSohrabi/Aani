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


class RawMaterialAndExcipientSpecifications(models.Model):
    TYPE_OF_RAW_MATERIAL_CHOICES = [
        ('not select', 'not select'),
        ('powder', 'powder'),
        ('granules_ready_for_process', 'granules_ready_for_process'),
        ('pellet', 'pellet'),
    ]
    temperature_humidity_sensitive = models.NullBooleanField()
    allowed_humidity_temperature_range = models.CharField(max_length=255, null=True, blank=True)
    light_sensitive = models.NullBooleanField()
    light_conditions = models.CharField(max_length=255, null=True, blank=True)
    api = models.NullBooleanField()
    oel = models.NullBooleanField()
    oel_value = models.FloatField(null=True, blank=True)
    valid_msds = models.NullBooleanField()
    source_country_raw_material = models.CharField(max_length=255, null=True, blank=True)
    type_raw_material = models.CharField(choices=TYPE_OF_RAW_MATERIAL_CHOICES, max_length=255, null=True, blank=True)
    presentation_washing_method = models.TextField(null=True, blank=True)


class SpecificationsOfDevicesAndEquipmentUsedInProduction(models.Model):
    TABLET_OR_CAPSULE = [
        ('not select', 'not select'),
        ('tablet', 'tablet'),
        ('capsule', 'capsule'),
    ]
    KIND_OF_COAT = [
        ('not select', 'not select'),
        ('uncoated', 'uncoated'),
        ('coated', 'coated'),
        ('slow release', 'slow release'),
        ('continuous release', 'continuous release'),
        ('other', 'other'),
    ]
    GRANULE_PRODUCTION_METHOD = [
        ('not select', 'not select'),
        ('wet granulation', 'wet granulation'),
        ('dry mix', 'dry mix'),
    ]
    GRANULATOR_TYPE = [
        ('not select', 'not select'),
        ('hmg', 'hmg'),
        ('fbd/g', 'fbd/g'),
    ]
    TEMPERATURE_GRANULATION = [
        ('not select', 'not select'),
        ('45-65c', '45-65c'),
        ('18-28c', '18-28c'),
    ]
    PRESS_SHAPE = [
        ('not select', 'not select'),
        ('normal concave', 'normal concave'),
        ('flat', 'flat'),
        ('oblong', 'oblong'),
    ]
    PUNCH_SPECIFICATIONS= [
        ('not select', 'not select'),
        ('non scored tablet', 'non scored tablet'),
        ('scored tablet', 'scored tablet'),
    ]
    SPECIFICATION_CAPSULE = [
        ('not select', 'not select'),
        ('granule', 'granule'),
        ('pellet', 'pellet'),
    ]
    CAPSULE_SIZE = [
        ('not select', 'not select'),
        ('0e', '0e'),
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    ]
    product_batch_weight = models.FloatField(null=True, blank=True)
    product_batch_number = models.FloatField(null=True, blank=True)
    production_anticipation = models.FloatField(null=True, blank=True)
    tablet_or_capsule = models.CharField(choices=TABLET_OR_CAPSULE, max_length=255, null=True, blank=True)
    kind_of_coat = models.CharField(choices=KIND_OF_COAT, max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    granule_production_method = models.CharField(choices=GRANULE_PRODUCTION_METHOD, max_length=255, null=True, blank=True) 
    granulator_type = models.CharField(choices=GRANULATOR_TYPE, max_length=255, null=True, blank=True)
    moisture_percentage_granule = models.CharField(max_length=255, null=True, blank=True)
    required_granulator_tank = models.CharField(max_length=255, null=True, blank=True)
    glue_making_tank_required = models.CharField(max_length=255, null=True, blank=True)
    temperature_granulation = models.CharField(choices=TEMPERATURE_GRANULATION, max_length=255, null=True, blank=True)
    mill_mesh_size = models.CharField(max_length=255, null=True, blank=True)
    fbd = models.NullBooleanField()
    mesh_for_api_sieving = models.CharField(max_length=255, null=True, blank=True)
    mesh_size_required_excipients_sieving = models.CharField(max_length=255, null=True, blank=True)
    required_blender = models.CharField(max_length=255, null=True, blank=True)
    press_size = models.CharField(max_length=255, null=True, blank=True)
    press_shape = models.CharField(choices=PRESS_SHAPE, max_length=255, null=True, blank=True)
    punch_specifications = models.CharField(choices=PUNCH_SPECIFICATIONS, max_length=255, null=True, blank=True)
    hardness_range_tablet_press = models.CharField(max_length=255, null=True, blank=True)
    diameter_tablet_press = models.CharField(max_length=255, null=True, blank=True)
    thickness_tablet_press = models.CharField(max_length=255, null=True, blank=True)
    tablet_weight_range = models.CharField(max_length=255, null=True, blank=True)
    specification_capsule = models.CharField(choices=SPECIFICATION_CAPSULE, max_length=255, null=True, blank=True)
    capsule_size = models.CharField(choices=CAPSULE_SIZE, max_length=255, null=True, blank=True)
    empty_shell_weight = models.CharField(max_length=255, null=True, blank=True)
    range_granule_weight_capsule = models.CharField(max_length=255, null=True, blank=True)
    storage_temperature = models.CharField(max_length=255, null=True, blank=True)
    humidity_temperature = models.CharField(max_length=255, null=True, blank=True)
    containers = models.CharField(max_length=255, null=True, blank=True)
    press = models.CharField(max_length=255, null=True, blank=True)
    capsule_filling = models.CharField(max_length=255, null=True, blank=True)
    coat = models.CharField(max_length=255, null=True, blank=True)

class PackagingMaterialsSpecifications(models.Model):
    TOC = [
        ('not select', 'not select'),
        ('tablet', 'tablet'),
        ('capsule', 'capsule'),
    ]
    MATERIAL_CONTAINER = [
        ('not select', 'not select'),
        ('plastic', 'plastic'),
        ('glass', 'glass'),
    ]
    CAP_MODEL = [
        ('not select', 'not select'),
        ('childproof', 'childproof'),
        ('simple', 'simple'),
    ]
    COTTON_SILICAGEL = [
        ('not select', 'not select'),
        ('plastic', 'plastic'),
        ('glass', 'glass'),
    ]
    BLISTER_TYPE = [
        ('not select', 'not select'),
        ('alu-alu', 'alu-alu'),
        ('alu-pvc', 'alu-pvc'),
        ('alu-pvdc', 'alu-pvdc'),
    ]
    PVC_TYPE = [
        ('not select', 'not select'),
        ('opaque', 'opaque'),
        ('transparent', 'transparent'),
        ('white', 'white'),
    ]
    TTAC = [
        ('not select', 'not select'),
        ('label', 'label'),
        ('print', 'print'),
    ]
    toc = models.CharField(choices=TOC, max_length=255, null=True, blank=True)
    container = models.NullBooleanField()
    material_container = models.CharField(choices=MATERIAL_CONTAINER, max_length=255, null=True, blank=True)
    container_size = models.CharField(max_length=255, null=True, blank=True)
    container_height = models.CharField(max_length=255, null=True, blank=True)
    opening_diameter = models.CharField(max_length=255, null=True, blank=True)
    cap_model = models.CharField(choices=CAP_MODEL, max_length=255, null=True, blank=True)
    number_tablet_capsules_percontainer = models.CharField(max_length=255, null=True, blank=True)
    cotton_silicagel = models.CharField(choices=COTTON_SILICAGEL, max_length=255, null=True, blank=True)
    number_silicagel = models.CharField(max_length=255, null=True, blank=True)
    blister_type = models.CharField(choices=BLISTER_TYPE, max_length=255, null=True, blank=True)
    pvc_type = models.CharField(choices=PVC_TYPE, max_length=255, null=True, blank=True)
    pvc_other = models.CharField(max_length=255, null=True, blank=True)
    blister_dimensions = models.CharField(max_length=255, null=True, blank=True)
    aluminum_foil_width = models.CharField(max_length=255, null=True, blank=True)
    pvc_width = models.CharField(max_length=255, null=True, blank=True)
    number_tablets_blister = models.CharField(max_length=255, null=True, blank=True)
    number_blister_box = models.CharField(max_length=255, null=True, blank=True)
    leaflet = models.NullBooleanField()
    number_box_carton = models.CharField(max_length=255, null=True, blank=True)
    final_contains = models.CharField(max_length=255, null=True, blank=True)
    ttac = models.CharField(choices=TTAC, max_length=255, null=True, blank=True)

class Experiments(models.Model):
    diameter = models.NullBooleanField()
    thickness = models.NullBooleanField()
    weight = models.NullBooleanField()
    hardness = models.NullBooleanField()
    friability = models.NullBooleanField()
    abrasion = models.NullBooleanField()
    disintegration_time = models.NullBooleanField()
    assay = models.NullBooleanField()
    qc_test = models.CharField(max_length=255, null=True, blank=True)
    t11 = models.CharField(max_length=255, null=True, blank=True)
    t12 = models.CharField(max_length=255, null=True, blank=True)
    t13 = models.CharField(max_length=255, null=True, blank=True)
    t21 = models.CharField(max_length=255, null=True, blank=True)
    t22 = models.CharField(max_length=255, null=True, blank=True)
    t23 = models.CharField(max_length=255, null=True, blank=True)
    t31 = models.CharField(max_length=255, null=True, blank=True)
    t32 = models.CharField(max_length=255, null=True, blank=True)
    t33 = models.CharField(max_length=255, null=True, blank=True)
    t41 = models.CharField(max_length=255, null=True, blank=True)
    t42 = models.CharField(max_length=255, null=True, blank=True)
    t43 = models.CharField(max_length=255, null=True, blank=True)
    t51 = models.CharField(max_length=255, null=True, blank=True)
    t52 = models.CharField(max_length=255, null=True, blank=True)
    t53 = models.CharField(max_length=255, null=True, blank=True)
    t61 = models.CharField(max_length=255, null=True, blank=True)
    t62 = models.CharField(max_length=255, null=True, blank=True)
    t63 = models.CharField(max_length=255, null=True, blank=True)
    t71 = models.CharField(max_length=255, null=True, blank=True)
    t72 = models.CharField(max_length=255, null=True, blank=True)
    t73 = models.CharField(max_length=255, null=True, blank=True)
    t81 = models.CharField(max_length=255, null=True, blank=True)
    t82 = models.CharField(max_length=255, null=True, blank=True)
    t83 = models.CharField(max_length=255, null=True, blank=True)
    t91 = models.CharField(max_length=255, null=True, blank=True)
    t92 = models.CharField(max_length=255, null=True, blank=True)
    t93 = models.CharField(max_length=255, null=True, blank=True)
    t101 = models.CharField(max_length=255, null=True, blank=True)
    t102 = models.CharField(max_length=255, null=True, blank=True)
    t103 = models.CharField(max_length=255, null=True, blank=True)
    t111 = models.CharField(max_length=255, null=True, blank=True)
    t112 = models.CharField(max_length=255, null=True, blank=True)
    t113 = models.CharField(max_length=255, null=True, blank=True)
    t121 = models.CharField(max_length=255, null=True, blank=True)
    t122 = models.CharField(max_length=255, null=True, blank=True)
    t123 = models.CharField(max_length=255, null=True, blank=True)


class TTMTContract(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('not select', 'not select'),
        ('medicine', 'medicine'),
        ('supplement', 'supplement'),
        ('herbal remedy', 'herbal remedy'),
    ]
    THERAPEUTIC_CATEGORY_CHOICES = [
        ('not select', 'not select'),
        ('hormonal', 'hormonal'),
        ('non-hormonal product', 'non-hormonal product'),
        ('non-antibiotics', 'non-antibiotics'),
        ('antibiotics', 'antibiotics'),
        ('hazardous', 'hazardous'),  
    ]
    F_AND_D_LICENSE_CHOICES = [
        ('not select', 'not select'),
        ('product license', 'product license'),
        ('contract manufacturing license', 'contract manufacturing license'),
        ('none', None)
    ]
    generic_name = models.CharField(max_length=255, null=True, blank=True)
    trade_name = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_type = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    product_type = models.CharField(choices=PRODUCT_TYPE_CHOICES,max_length=255, null=True, blank=True)
    therapeutic_category = models.CharField(choices=THERAPEUTIC_CATEGORY_CHOICES ,max_length=255, null=True, blank=True)
    food_and_drug_administration_licenses = models.CharField(choices=F_AND_D_LICENSE_CHOICES, max_length=255, null=True, blank=True)
    representative = models.CharField(max_length=255, null=True, blank=True)
    authorized_person = models.CharField(max_length=255, null=True, blank=True)
    raw_material_and_excipient_specifications = models.ForeignKey(RawMaterialAndExcipientSpecifications, null=True, blank=True, on_delete=models.CASCADE)
    specifications_of_devices_and_equipment_used_in_production = models.ForeignKey(SpecificationsOfDevicesAndEquipmentUsedInProduction, null=True, blank=True, on_delete=models.CASCADE)
    packaging_materials_specifications = models.ForeignKey(PackagingMaterialsSpecifications, null=True, blank=True, on_delete=models.CASCADE)
    experiments = models.ForeignKey(Experiments, null=True, blank=True, on_delete=models.CASCADE)