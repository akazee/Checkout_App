from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import is_valid_path
from .models import *
from .forms import *

# view config for base html
def index(response, id):
    ls = recipt.objects.get(id=id)
    newItemform = AddItem()
    newDiscform = AddDiscount()

    # If a user submits any form, we retrieve the data
    if response.method == "POST":
        # If a new item was submitted
        if(response.POST.get("saveItem")):
            newItemform = AddItem(response.POST)         

            if newItemform.is_valid():
                newName = newItemform.cleaned_data["name"]
                newPrice = newItemform.cleaned_data["price"]

                newItem = item(name=newName, price=newPrice)
                newItem.save()
                ls.items.add(newItem)

        # If a new discount was submitted
        elif(response.POST.get("saveDiscount")):
            newDiscform = AddDiscount(response.POST)

            if newDiscform.is_valid():
                disc = newDiscform.cleaned_data["discount"]
                newDisc = discount(discount=disc)
                newDisc.save()
                ls.discount.add(newDisc)
    
    # Else, if no form is selected continue as always 
    return render(response, "checkout/display.html", {"ls":ls, "subtotal":ls.subtotal, "disctotal":ls.discount_total, "Itemform":newItemform, "DiscForm": newDiscform})
    
# view config for home 
def home(request):
   return render(request, 'checkout/checkout_home.html', {})

# Form that creates a new order
def create(response):
    # If someone decides to create a new order, we redirect to that orders new page
    if response.method == "POST":
        form = CreateNewOrder(response.POST)

        if form.is_valid():
            txt = form.cleaned_data["name"]
            r = recipt(text=txt)
            r.save()

            return HttpResponseRedirect("/%i" %r.id)
    else:
    # else if we stay here
        form = CreateNewOrder()
    return render(response, "checkout/create.html", {"form":form})