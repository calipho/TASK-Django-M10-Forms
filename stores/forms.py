from django import forms
from .models import StoreItem


class StoreItemForm(forms.ModelForm):
    class Meta:
        model = StoreItem
        fields = ['name', 'description', 'kind', 'price']


class StoreItemUpdateForm(forms.ModelForm):
    class Meta:
        model = StoreItem
        fields = ['name', 'description', 'kind', 'price']


class StoreItemDeleteForm(forms.ModelForm):
    class Meta:
        model = StoreItem
        fields = ['name', 'description', 'kind', 'price']
