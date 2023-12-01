from django.forms import ModelForm, widgets
from django.core.exceptions import ValidationError
from django import forms
from .models import *


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = [
            'image',
            'generic_name',
            'name',
            'purchase_price',
            'sell_price',
            'medicine_type',
            'category',
            'prescription_required',
            'strength',
            'pack_size',
            'expiry_date',
            'stock_quantity',
            'total_quantity',
            'manufacturer',
            'is_available',
            'patient_package_insert',
            'description',
            'is_featured',
            'discount_percentage',
        ]
        labels = {
            'patient_package_insert': 'Description PDF File'
        }
        widgets = {
            'alternate_brands': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(MedicineForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['image', 'name', 'description']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class MedicineTypeForm(forms.ModelForm):
    class Meta:
        model = MedicineType
        fields = ['image', 'name', 'description']

    def __init__(self, *args, **kwargs):
        super(MedicineTypeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['image', 'name', 'description',
                  'contact_number', 'email', 'website']

    def __init__(self, *args, **kwargs):
        super(ManufacturerForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
