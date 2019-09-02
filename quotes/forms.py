from django import forms
from .models import Stock


# Setup stock form
class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["symbol"]
