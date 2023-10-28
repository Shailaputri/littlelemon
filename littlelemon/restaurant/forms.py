from django import forms
from restaurant.models import Menu, BookingTable

# ModelForm: MenuForm
class MenuForm(forms.Form):
    title = forms.CharField(max_length =255)
    price = forms.CharField(max_length = 10)
    inventory = forms.CharField(max_length = 4)

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingTable
        fields = "__all__"
        
