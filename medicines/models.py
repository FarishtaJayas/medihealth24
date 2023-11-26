from django.db import models
import uuid
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class MedicineType(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    generic_name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(max_length=3000, blank=True, null=True)
    side_effects = models.TextField(max_length=3000, blank=True, null=True)
    strength = models.CharField(max_length=250, null=True, blank=True)
    sell_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    purchase_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    pack_size = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default="default.png")
    stock_quantity = models.IntegerField(default=0)
    total_quantity = models.IntegerField(default=0)
    alternate_brands = models.ManyToManyField(
        Manufacturer, related_name='alternate_brands', blank=True, through='MedicineAlternateBrand')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    composition = models.TextField(null=True, blank=True)
    prescription_required = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    rating = models.FloatField(null=True, blank=True)
    discount_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    batch_number = models.CharField(max_length=250, null=True, blank=True)
    express_delivery = models.BooleanField(default=False)
    medicine_type = models.OneToOneField(
        MedicineType, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.generic_name


class MedicineAlternateBrand(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.medicine} - {self.manufacturer}"
