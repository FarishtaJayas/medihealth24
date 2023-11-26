from django.forms import ModelForm, widgets
from django import forms
from .models import Medicine


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = ['generic_name', 'description',
                  'side_effects', 'medicine_type', 'strength', 'sell_price', 'purchase_price', 'pack_size', 'image',
                  'stock_quantity', 'total_quantity', 'alternate_brand', 'category', 'expiry_date', 'manufacturer_name',
                  'manufacturer_address', 'composition', 'prescription_required', 'is_featured', 'rating', 'discount_percentage',
                  'is_available', 'batch_number']

    def __init__(self, *args, **kwargs):
        super(MedicineForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
