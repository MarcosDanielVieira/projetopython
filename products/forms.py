from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Digite o título do produto"}
            ),
            "price": forms.NumberInput(attrs={"placeholder": "Digite o preço"}),
            "description": CKEditor5Widget(attrs={"placeholder": "Digite a descrição"}),
        }
