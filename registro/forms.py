from django import forms
from .models import Category, Spent


class LoadForm(forms.Form):
    category = category = forms.ModelChoiceField(
        label='',
        queryset=Category.objects.all(),
        empty_label="Seleccione una categoría")
    mount = forms.IntegerField(label='')
