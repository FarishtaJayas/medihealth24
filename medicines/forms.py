from django.forms import ModelForm, widgets
from .generic_names import generic_names
from django.core.exceptions import ValidationError
from django import forms
from .models import *
from django_select2 import forms as select2forms



class MedicineForm(ModelForm):
    generic_name = forms.ChoiceField(
        choices=[(name, name[:80]) for name in generic_names],
        widget=select2forms.Select2Widget  # Add this line to use Select2
    )

    class Meta:
        model = Medicine
        fields = [
            'image',
            'generic_name',
            'name',
            'strength',
            'manufacturer',
            'sell_price',
            'prescription_required',
            'medicine_type',
            'pack_size',
            'unit_of_measurement',
            'category',
            'patient_package_insert',
        ]
        labels = {
            'patient_package_insert': 'Description PDF File',
            'unit_of_measurement': 'Unit of Measurement (UOM)'
        }

    def __init__(self, *args, **kwargs):
        super(MedicineForm, self).__init__(*args, **kwargs)

        self.fields['generic_name'].widget.attrs.update(
            {'class': 'responsive-generic-name'})

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