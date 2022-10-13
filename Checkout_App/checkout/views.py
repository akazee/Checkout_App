from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib import messages


# view config for home 
def home(request):
   return render(request, 'checkout/create.html', {})

# view config for base html
def index(response, id):

    # initliazie all forms and get the recipt object for this order
    ls = recipt.objects.get(id=id)
    newItemform = AddItem()
    newDiscform = AddDiscount()
    delItemForm = RemoveItem()
    delDiscForm = RemoveDiscount()

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

        # If user wants to delete an item from the order
        elif(response.POST.get("delitem")):
            delItemForm = RemoveItem(response.POST)

            # We delete the item from recipt, only if our recipt has the id of that item
            if delItemForm.is_valid():
                x = delItemForm.cleaned_data["id"]
                if(ls.hasItem(x)):
                    ls.removeItem(x)

        # If a new discount was submitted
        elif(response.POST.get("saveDiscount")):
            newDiscform = AddDiscount(response.POST)

            if newDiscform.is_valid():
                disc = newDiscform.cleaned_data["discount"]
                newDisc = discount(discount=disc)
                newDisc.save()
                ls.discount.add(newDisc)

        # If user wants to delete a discount from the order
        elif(response.POST.get("deldisc")):
            delDiscForm = RemoveItem(response.POST)

            # We delete the discount from recipt, only if our recipt has the id of that discount
            if delDiscForm.is_valid():
                x = delDiscForm.cleaned_data["id"]
                if(ls.hasDiscount(x)):
                    ls.removeDiscount(x)

    # Render the page with once a any form has been submitted, updates the information
    tax = round(float(ls.discount_total) * 0.13, 2)
    total = round(float(ls.discount_total) + tax, 2)
    return render(response, "checkout/display.html", {"ls":ls, "subtotal":ls.subtotal,
     "disctotal":ls.discount_total, "tax":tax, "total":total, "form1":newItemform,
     "form2": newDiscform, "form3":delItemForm, "form4":delDiscForm})

# Form that creates a new order
def create(response):
    form = CreateNewOrder()
    oldform = loadOrder()

    # If someone decides to create a new order, we redirect to that orders new page
    if (response.method == "POST") and (response.POST.get("save")):
        form = CreateNewOrder(response.POST)

        if form.is_valid():
            txt = form.cleaned_data["name"]
            r = recipt(text=txt)
            r.save()

            return HttpResponseRedirect("/%i" %r.id)
    # If user decides to load an old order, we redirect to the old order page
    elif (response.method == "POST") and (response.POST.get("Load")):
        oldform = loadOrder(response.POST)

        if oldform.is_valid():
            newId = oldform.cleaned_data["id"]
            if(newId <= recipt.objects.all().count()):
                return HttpResponseRedirect("/" + str(newId))

    # Otherwise, we stay here
    recipts = recipt.objects.all()
    return render(response, "checkout/create.html", {"form":form, "recipts": recipts, "oldform":oldform})