from django import forms
from . import models

class SanPhanForm(forms.ModelForm):

    class Meta:

        model = models.SanPham
        fields = '__all__'