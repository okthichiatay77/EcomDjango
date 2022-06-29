from django import forms
from . import models

class SanPhanForm(forms.ModelForm):

    class Meta:

        model = models.SanPham
        fields = '__all__'


class CartForm(forms.ModelForm):

    class Meta:

        model = models.Cart
        fields = '__all__'