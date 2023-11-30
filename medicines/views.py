from django.shortcuts import render
from django.shortcuts import redirect
from .models import Medicine
from .forms import *
# Create your views here.


def medicines(request):
    medicines = Medicine.objects.all()
    context = {'medicines': medicines}
    return render(request, 'medicines/medicines.html', context)


def medicine(request, pk):
    medicine = Medicine.objects.get(id=pk)
    context = {'medicine': medicine}
    return render(request, 'medicines/medicine.html', context)


def create_medicine(request):
    form = MedicineForm()

    if request.method == "POST":
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-medicine')
    context = {
        'form': form,
        'action': 'Add',
        'object': 'Medicine'
    }
    return render(request, 'medicines/create_form.html', context)


def update_medicine(request, pk):
    medicine = Medicine.objects.get(id=pk)
    form = MedicineForm(instance=medicine)

    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicines')

    context = {'form': form, 'object': 'Medicine', 'action': 'Edit'}
    return render(request, 'medicines/create_form.html', context)


def delete_medicine(request, pk):
    medicine = Medicine.objects.get(id=pk)

    if request.method == "POST":
        medicine.delete()
        return redirect('create-medicine')

    context = {
        'object': medicine
    }

    return render(request, 'medicines/delete_template.html', context)


def create_category(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryFomr(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-medicine')

    context = {
        'form': form,
        'action': 'Add',
        'object': 'Category'
    }

    return render(request, 'medicines/create_form.html', context)


def create_medicine_type(request):
    form = MedicineTypeForm()

    if request.method == "POST":
        form = MedicineTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-medicines')
    context = {
        'form': form,
        'action': 'Add',
        'object': 'Medicine Type'
    }

    return render(request, 'medicines/create_form.html', context)


def create_manufacturer(request):
    form = ManufacturerForm()

    if request.method == "POST":
        form = ManufacturerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-medicines')
    context = {
        'form': form,
        'action': 'Add',
        'object': 'Manufacturer'
    }

    return render(request, 'medicines/create_form.html', context)
