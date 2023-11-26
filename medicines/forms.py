from django.forms import ModelForm, widgets
from django.core.exceptions import ValidationError
from django import forms
from .models import Medicine


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = [
            'image',
            'batch_number',
            'generic_name',
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
            'composition',
            'description',
            'side_effects',
            'alternate_brands',
            'is_featured',
            'rating',
            'discount_percentage',
        ]
        widgets = {
            'alternate_brands': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(MedicineForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
