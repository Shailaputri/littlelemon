from django import forms

# ModelForm: MenuForm
class MenuForm(forms.Form):
    title = forms.CharField(max_length =255)
    price = forms.CharField(max_length = 10)
    inventory = forms.CharField(max_length = 4)