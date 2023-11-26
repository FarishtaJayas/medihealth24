from django.urls import path
from .views import medicines, medicine, create_medicine, update_medicine, delete_medicine

urlpatterns = [
    path('', medicines, name='medicines'),
    path('<uuid:pk>/', medicine, name='medicine'),

    path('create-medicine/', create_medicine, name='create-medicine'),
    path('update-medicine/<uuid:pk>', update_medicine, name='update-medicine'),
    path('delete-medicine/<uuid:pk>', delete_medicine, name='delete-medicine'),
]
