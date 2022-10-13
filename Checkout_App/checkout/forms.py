from django import forms
from  .models import *

# Form that will create new recipt model
class CreateNewOrder(forms.Form):
    name = forms.CharField(label="Order Name", max_length=200)

# Form that will create a new item for an order
class AddItem(forms.Form):
    name = forms.CharField(label="Item Name", max_length=200)
    price = forms.DecimalField(label="Price of Item", max_digits=10, decimal_places=2, min_value=0)

# Form that will add a discount to a recipt
class AddDiscount(forms.Form):
    discount = forms.DecimalField(label="Discount(%)", max_digits=5, decimal_places=2, min_value=0)

# Form that will remove an item from an order
class RemoveItem(forms.Form):
    id = forms.IntegerField(label="ID of item to remove", max_value=1000)

class RemoveDiscount(forms.Form):
    id = forms.IntegerField(label="ID of discount to remove", max_value=1000)

# Form that will load a previous order for a user
class loadOrder(forms.Form):
    id = forms.IntegerField(label="Order ID", max_value=1000, min_value=1)

