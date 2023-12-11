from django.db import models
import uuid
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
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
    image = models.ImageField(
        upload_to='medicine_type_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='manufacturer_images/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    generic_name = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(max_length=3000, blank=True, null=True)
    patient_package_insert = models.FileField(
        upload_to='medicine_pdf_files/', null=True, blank=True)
    side_effects = models.TextField(max_length=3000, blank=True, null=True)
    strength = models.CharField(max_length=250, null=True, blank=True)
    sell_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    purchase_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    pack_size = models.CharField(max_length=250, null=True, blank=True)
    unit_of_measurement = models.CharField(
        max_length=250, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default="default.png")
    stock_quantity = models.IntegerField(default=0)
    total_quantity = models.IntegerField(default=0)
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
    medicine_type = models.ForeignKey(
        MedicineType, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.generic_name

    class Meta:
        ordering = ['-created']
        # the dash makes it descending
