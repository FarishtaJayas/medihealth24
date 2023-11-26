from django.forms import ModelForm
from .models import Medicine


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = ['generic_name', 'description',
                  'side_effects', 'dosage_form', 'strength', 'sell_price', 'purchase_price', 'pack_size', 'image',
                  'stock_quantity', 'total_quantity', 'alternate_brand', 'category', 'expiry_date', 'manufacturer_name',
                  'manufacturer_address', 'composition', 'prescription_required', 'is_featured', 'rating', 'discount_percentage',
                  'is_available', 'batch_number']
