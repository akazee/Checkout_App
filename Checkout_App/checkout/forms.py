from django import forms

class CreateNewOrder(forms.Form):
    name = forms.CharField(label="Order Name", max_length=200)

class AddItem(forms.Form):
    name = forms.CharField(label="Item Name", max_length=200)
    price = forms.DecimalField(label="Price of Item", max_digits=10, decimal_places=2, min_value=0)

class AddDiscount(forms.Form):
    discount = forms.DecimalField(label="Discount(%)", max_digits=5, decimal_places=2, min_value=0)

# class Remove Item(forms.Form):
#     id = forms.IntegerField(label="ID of item", max_value=1000)

