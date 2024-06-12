from django.test import TestCase
from rest_framework.test import APIClient
from .models import Item, Supplier, StoreInventory

class StoreInventoryAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_storeinventory_list_create(self):
        # Create an item
        item = Item.objects.create(name='Test Item')

        # Create a supplier
        supplier = Supplier.objects.create(
            supplier_name='Test Supplier',
            contact_information='test@example.com'
        )
        supplier.items_they_supply.add(item)

        # Create a store inventory item
        data = {
            'supplier': {
                'id': supplier.id,
                'supplier_name': 'Supplier Name',  
                'contact_information': 'Contact@gmail.com'  
            },
            'inventory_item': {
                'id': item.id,
                'name': 'Item Name'  
            },
            'description': 'Test description',
            'price': '10.50',
            'quantity': 100
        }


        
        response = self.client.post('/api/storeinventory/', data, format='json')

        print("Create response data:", response.data)
        print("Create response status code:", response.status_code)  # Added these lines for debugging

        self.assertEqual(response.status_code, 201)

        # Retrieve all store inventory items
        response = self.client.get('/api/storeinventory/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


    def test_storeinventory_retrieve_update_delete(self):
        
        item = Item.objects.create(name='Test Item')

        # Created a supplier
        supplier = Supplier.objects.create(
            supplier_name='Test Supplier',
            contact_information='test@example.com'
        )
        supplier.items_they_supply.add(item)

        # Created a store inventory item
        store_inventory = StoreInventory.objects.create(
            supplier=supplier,
            inventory_item=item,
            description='Test description',
            price='10.50',
            quantity=100
        )
        print("Created store inventory item:", store_inventory)

        # Retrieve the created store inventory item via response
        response = self.client.get(f'/api/storeinventory/{store_inventory.pk}/')
        print("Retrieved store inventory item. Response status code:", response.status_code)
        print("Retrieved data:", response.data)
        self.assertEqual(response.status_code, 200)

        # Update the store inventory item as json response
        updated_data = {
            'supplier': {'id': supplier.id, 'supplier_name': supplier.supplier_name, 'contact_information': supplier.contact_information},
            'inventory_item': {'id': item.id, 'name': item.name}, 
            'description': 'Updated description',
            'price': '15.00',
            'quantity': 200
        }



        print("Updating store inventory item with data:", updated_data)
        response = self.client.put(f'/api/storeinventory/{store_inventory.pk}/', updated_data, format='json')
        print("Update response status code:", response.status_code)
        print("Update response data:", response.data)
        self.assertEqual(response.status_code, 200)
        #NB: added the prints for debugging

        # Deleting the store inventory item
        print("Deleting store inventory item:", store_inventory.pk)
        response = self.client.delete(f'/api/storeinventory/{store_inventory.pk}/')
        print("Delete response status code:", response.status_code)
        self.assertEqual(response.status_code, 204)


class SupplierAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_supplier_list_create(self):
        
        item = Item.objects.create(name='Test Item')

        # Create a supplier
        data = {
            'supplier_name': 'Test Supplier',
            'contact_information': 'test@example.com',
            'items_they_supply': [item.id]  # Included items they supply
        }
        
        response = self.client.post('/api/supplier/', data, format='json')
        self.assertEqual(response.status_code, 201)

        # Retrieve all suppliers
        response = self.client.get('/api/supplier/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_supplier_retrieve_update_delete(self):
        # Create an item
        item = Item.objects.create(name='Test Item')

        # Create a supplier
        supplier = Supplier.objects.create(
            supplier_name='Test Supplier',
            contact_information='test@example.com'
        )
        supplier.items_they_supply.add(item)

        # Retrieve the created supplier
        response = self.client.get(f'/api/supplier/{supplier.pk}/')
        self.assertEqual(response.status_code, 200)

        # Update the supplier
        updated_data = {
            'supplier_name': 'Updated Supplier',
            'contact_information': 'updated@example.com',
            'items_they_supply': [item.id]  
        }
        
        response = self.client.put(f'/api/supplier/{supplier.pk}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)

        # Delete the supplier
        response = self.client.delete(f'/api/supplier/{supplier.pk}/')
        self.assertEqual(response.status_code, 204)
