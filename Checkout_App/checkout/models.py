from ast import Delete
from re import X
from django.db import models
from django.db.models import Sum

# Class for Item instances
class item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

# Class for a discount that can be applied to a recipt
class discount(models.Model):
    discount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "discount of " + str(self.discount) + "%"

# Class for a recipt, which is made up of item instances
class recipt(models.Model):
    # A recpit is made up of many items
    items = models.ManyToManyField(item)

    # A recipt can have a discount
    discount = models.ManyToManyField(discount)

    # description of our recipt
    text = models.CharField(max_length=300)
    

    def __str__(self):
        return self.text

    # subtotal of all items for this recipt
    @property
    def subtotal(self):
        return round(sum([x.price for x in self.items.all()]), 2)
    
    # Total with discount
    @property
    def discount_total(self):
        x = (sum([x.discount for x in self.discount.all()])/100)
        if(x == 0):
            return self.subtotal
        else:
            return round(self.subtotal * (1 - x), 2)

    # Check to see if this recipt holds the item, given by id
    def hasItem(self, itemId):
        return any(x.id == itemId for x in self.items.all())
    
    # Removes the item with itemID from this recipts list of items
    def removeItem(self, itemID):
        any(self.items.remove(x) for x in self.items.all() if x.id == itemID)
        pass 

    # returns a string that lists out all of the items and discounts in this list, 
    # as well as displaying the totals
    def list_all(self):
        text = "<ul>"
        for item in self.items.all():
            text += "<li>ID " + str(item.id) + " " + str(item.name) + ": " + str(item.price) + "</li>"
        
        text += "</ul>"
        text += "</br>subtotal: " + str(self.subtotal)
        text += "</br>Discount Total: " + str(self.discount_total)
        return text

