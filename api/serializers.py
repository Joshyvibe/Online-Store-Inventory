from rest_framework import serializers
from .models *

class SupplierSerializer(serializers.ModelSerializer):
    # Set items_they_supply required to false so that it wont affect inventory post processing
    items_they_supply = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True, required=False)
   
    class Meta:
        model = Supplier
        fields = ['id', 'supplier_name', 'contact_information', 'items_they_supply']  

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']  

class StoreInventorySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    inventory_item = ItemSerializer()

    class Meta:
        model = StoreInventory
        fields = ['id', 'supplier', 'inventory_item', 'description', 'price', 'quantity', 'date_added']
    
    def create(self, validated_data):
        # Extract the supplier data
        supplier_data = validated_data.pop('supplier')

        # Extract the inventory item data
        inventory_item_data = validated_data.pop('inventory_item')

        # Create or update supplier instance
        supplier_instance, _ = Supplier.objects.update_or_create(**supplier_data)

        # Create or update inventory item instance
        inventory_item_instance, _ = Item.objects.update_or_create(**inventory_item_data)

        # Create StoreInventory instance
        store_inventory = StoreInventory.objects.create(
            supplier=supplier_instance,
            inventory_item=inventory_item_instance,
            **validated_data
        )

        return store_inventory


    def update(self, instance, validated_data):
        # Update supplier if supplied
        supplier_data = validated_data.pop('supplier', None)
        if supplier_data:
            supplier_instance = instance.supplier
            supplier_serializer = self.fields['supplier']
            updated_supplier = supplier_serializer.update(supplier_instance, supplier_data)
        
        # Update inventory item if supplied
        inventory_item_data = validated_data.pop('inventory_item', None)
        if inventory_item_data:
            inventory_item_instance = instance.inventory_item
            inventory_item_serializer = self.fields['inventory_item']
            updated_inventory_item = inventory_item_serializer.update(inventory_item_instance, inventory_item_data)

        # Update other fields of StoreInventory
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.date_added = validated_data.get('date_added', instance.date_added)
        instance.save()

        return instance



    
