from django.urls import path
from .views import *

urlpatterns = [
    path('', medicines, name='medicines'),
    path('<uuid:pk>/', medicine, name='medicine'),

    path('create-medicine/', create_medicine, name='create-medicine'),
    path('update-medicine/<uuid:pk>', update_medicine, name='update-medicine'),
    path('delete-medicine/<uuid:pk>', delete_medicine, name='delete-medicine'),

    path('create-category/', create_category, name='create-category'),
    path('create-medicine_type/', create_medicine_type,
         name='create-medicine-type'),
    path('create-manufacturer/', create_manufacturer, name='create-manufacturer'),
]
