from django import forms
from ckeditor.widgets import CKEditorWidget
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
            "description": CKEditorWidget(attrs={"placeholder": "Digite a descrição"}),
        }
