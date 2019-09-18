from django import forms
from .models import Vendas


class VendaForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = "__all__"
        widgets = {'comprador': forms.HiddenInput(), 'vendedor': forms.HiddenInput(), 'produto_vendido': forms.HiddenInput()}
