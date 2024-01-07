from django import forms
from django.forms import ModelForm, ModelChoiceField

from .models import *


class ManufacturerSearchInput(forms.TextInput):
    input_type = 'search'


class ManufacturerChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class MedicineForm(ModelForm):
    manufacturer = ManufacturerChoiceField(
        label='Manufacturer',
        queryset=Manufacturer.objects.all(),
        widget=ManufacturerSearchInput(attrs={'class': 'input searchable-input'}),
    )

    class Meta:
        model = Medicine
        fields = [
            'image',
            'name',
            'generic_name',
            'strength',
            'manufacturer',
            'sell_price',
            'prescription_required',
            'refrigerated',
            'returnable_item',
            'medicine_type',
            'pack_size',
            'unit_of_measurement',
            'category',
            'patient_package_insert',
        ]
        labels = {
            'returnable_item': 'Can Return Item?',
            'patient_package_insert': 'Description PDF File',
            'unit_of_measurement': 'Unit of Measurement (UOM)',
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


class GenericNameForm(forms.Form):
    generic_name = forms.CharField(
        label='Generic Name',
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
