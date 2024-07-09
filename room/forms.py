from django import forms
from . import models

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name', 'amount']

class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name', 'amount']

class AddRoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = ['category', 'name']

class UpdateRoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = ['category', 'name']

class NewBookingForm(forms.ModelForm):
    class Meta:
        model = models.Booking
        exclude = ('room', 'timestamp',)

class UpdateBookingForm(forms.ModelForm):
    class Meta:
        model = models.Booking
        exclude = ('room', 'timestamp',)