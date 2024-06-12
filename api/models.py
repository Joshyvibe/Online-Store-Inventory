from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=100)
    #Comment: I created this item model because I want to separate it from 
    #Supplier and StoreInventory model that way it will be independent 
    # But the two models would be dependent of it. 

    def __str__(self):
        return self.name
    

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=255)
    items_they_supply = models.ManyToManyField(Item, related_name='suppliers')
    #Comment: I've created a relationship between the supplier and item model.
    # In it i'm using many to many fields to pull the items making it 
    # possible for any supplier to have multiple items and supply similar items. 

    def __str__(self):
        return self.supplier_name


class StoreInventory(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    inventory_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    #Comment: For the StoreInventory model, I added more fields to capture
    # price and quantity cos everything item supplied usually should have a price
    # and quantity attached to them.

    class Meta:
        verbose_name_plural = "Store inventories"

    def __str__(self):
        return f"{self.inventory_item.name} from {self.supplier.supplier_name}"
    
   

