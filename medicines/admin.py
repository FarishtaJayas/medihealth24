from django.contrib import admin
from .models import Medicine, Category, MedicineType
# Register your models here.

admin.site.register(Medicine)
admin.site.register(Category)
admin.site.register(MedicineType)
