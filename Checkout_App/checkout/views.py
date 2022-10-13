from django.shortcuts import render
from django.http import HttpResponse
from .models import recipt

# view config for base html
def index(response, id):
    ls = recipt.objects.get(id=id)
    return render(response, "checkout/display.html", {"ls":ls, "subtotal":ls.subtotal, "disctotal":ls.discount_total})
    
# view config for home 
def home(request):
   return render(request, 'checkout/checkout_home.html', {})

