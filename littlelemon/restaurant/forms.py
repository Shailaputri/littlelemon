from django import forms
from restaurant.models import Menu, BookingTable, Category

# ModelForm: MenuForm
class MenuForm(forms.Form):
    title = forms.CharField(max_length =255)
    price = forms.CharField(max_length = 10)
    inventory = forms.CharField(max_length = 4)
    description = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    # featured = forms.ModelChoiceField(queryset = [True, False])
    # class Meta:
    #     model = Menu
    #     fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingTable
        fields = "__all__"
        
