from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *



#NB: I used APIView cos it offers me the opportunity to implement complex logic beyond 
# what's offered by the generic views. APIView gives me full control over the behavior of each endpoint.

class ItemListCreateAPIView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ItemDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class StoreInventoryListCreateAPIView(APIView):
    def get(self, request):
        store_inventory = StoreInventory.objects.all()
        serializer = StoreInventorySerializer(store_inventory, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StoreInventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreInventoryRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return StoreInventory.objects.get(pk=pk)
        except StoreInventory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        store_inventory = self.get_object(pk)
        serializer = StoreInventorySerializer(store_inventory)
        return Response(serializer.data)

    def put(self, request, pk):
        store_inventory = self.get_object(pk)
        serializer = StoreInventorySerializer(store_inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        store_inventory = self.get_object(pk)
        store_inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SupplierListCreateAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            supplier = Supplier.objects.get(pk=pk)
            supplied_items = StoreInventory.objects.filter(supplier=supplier)
            serializer = StoreInventorySerializer(supplied_items, many=True)
            return Response(serializer.data)
        else:
            suppliers = Supplier.objects.all()
            serializer = SupplierSerializer(suppliers, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   

# This list_supplied_items class is helping to pull up all items currently
# supplied by a supplier. I'm using pk to check the storeinventory for items 
# supplied by the supplier.
class SupplierItemsSuppliedAPIView(APIView):
    def get(self, request, pk):
        try:
            supplier = Supplier.objects.get(pk=pk)
            supplied_items = StoreInventory.objects.filter(supplier=supplier)
            serializer = StoreInventorySerializer(supplied_items, many=True)
            return Response(serializer.data)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class SupplierRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    def put(self, request, pk):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        supplier = self.get_object(pk)
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
