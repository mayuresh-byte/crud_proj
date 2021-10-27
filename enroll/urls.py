from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_show, name='addandshow'),
    path('delete/<int:id>', views.delt, name='delete'),
    path('edit/<int:id>', views.edt, name='edit'),
]

