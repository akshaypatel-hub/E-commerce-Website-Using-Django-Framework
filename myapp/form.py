from django import forms
from .models import Productlogin,Product,Cart


class Productform(forms.ModelForm):
    class Meta:
        model = Productlogin
        fields = '__all__'


class Productdetails(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



class Cartfrom(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'