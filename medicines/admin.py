from django.contrib import admin
from .models import Medicine, Category, MedicineType, Manufacturer
# Register your models here.

admin.site.register(Medicine)
admin.site.register(Category)
admin.site.register(MedicineType)
admin.site.register(Manufacturer)
