from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import *
from .utils import search_medicines, paginate_medicines


# Create your views here.


def medicines(request):
    medicines, search_query = search_medicines(request)
    custom_range, medicines = paginate_medicines(request, medicines, 6)
    medicine_count = Medicine.objects.count()
    context = {'medicines': medicines,
               'search_query': search_query,
               'custom_range': custom_range,
               'medicine_count': medicine_count,
               }
    return render(request, 'medicines/medicines.html', context)


def medicine(request, pk):
    medicine = Medicine.objects.get(id=pk)
    context = {'medicine': medicine}
    return render(request, 'medicines/medicine.html', context)


@login_required(login_url='login')
def create_medicine(request):
    form = MedicineForm()

    if request.method == "POST":
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            strength = form.cleaned_data['strength']
            manufacturer = form.cleaned_data['manufacturer']
            medicine_type = form.cleaned_data['medicine_type']

            matching_medicines = Medicine.objects.filter(
                name=name, strength=strength, manufacturer=manufacturer, medicine_type=medicine_type)
            if matching_medicines.exists():
                for med in matching_medicines:

                    if (
                            med.name == name and med.strength == strength and med.manufacturer == manufacturer and med.medicine_type == medicine_type):
                        messages.error(
                            request,
                            'Medicine with this combination already exists. Please enter a different combination.')
                        return render_with_data(request, form)
            else:
                form.save()
                messages.success(
                    request, 'Medicine was added successfully')
                return redirect('create-medicine')

    context = {
        'form': form,
        'action': 'Add',
        'object': 'Medicine'
    }
    return render(request, 'medicines/create_form.html', context)


@login_required(login_url='login')
def update_medicine(request, pk):
    medicine = Medicine.objects.get(id=pk)
    form = MedicineForm(instance=medicine)

    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES, instance=medicine)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicine was edited successfully')
            return redirect('medicines')

    context = {'form': form, 'object': 'Medicine', 'action': 'Edit'}
    return render(request, 'medicines/create_form.html', context)


@login_required(login_url='login')
def delete_medicine(request, pk):
    medicine = Medicine.objects.get(id=pk)

    if request.method == "POST":
        medicine.delete()
        messages.success(request, 'Medicine was deleted successfully')
        return redirect('medicines')

    context = {
        'object': medicine
    }

    return render(request, 'medicines/delete_template.html', context)


@login_required(login_url='login')
def create_category(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category was added successfully')
            return redirect('create-medicine')

    context = {
        'form': form,
        'action': 'Add',
        'object': 'Category'
    }

    return render(request, 'medicines/create_form.html', context)


@login_required(login_url='login')
def create_medicine_type(request):
    form = MedicineTypeForm()

    if request.method == "POST":
        form = MedicineTypeForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Medicine type was added successfully')
            form.save()
            return redirect('medicines')
    context = {
        'form': form,
        'action': 'Add',
        'object': 'Medicine Type'
    }

    return render(request, 'medicines/create_form.html', context)


@login_required(login_url='login')
def create_manufacturer(request):
    form = ManufacturerForm()

    if request.method == "POST":
        form = ManufacturerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manufacturer was added successfully')
            return redirect('medicines')
    context = {
        'form': form,
        'action': 'Add',
        'object': 'Manufacturer'
    }

    return render(request, 'medicines/create_form.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('medicines')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('medicines')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'User was logged out')
    return redirect('login')


def render_with_data(request, form):
    context = {
        'form': form,
        'action': 'Add',
        'object': 'Medicine'
    }
    return render(request, 'medicines/create_form.html', context)
