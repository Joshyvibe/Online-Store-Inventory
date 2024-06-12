from django.urls import path
from .views import *


urlpatterns = [
    path('item/', ItemListCreateAPIView.as_view(), name='item-list-create'),
    path('item/<int:pk>/', ItemDetailAPIView.as_view(), name='item-detail'),
    path('storeinventory/', StoreInventoryListCreateAPIView.as_view(), name='storeinventory-list-create'),
    path('storeinventory/<int:pk>/', StoreInventoryRetrieveUpdateDeleteAPIView.as_view(), name='storeinventory-retrieve-update-delete'),
    path('supplier/', SupplierListCreateAPIView.as_view(), name='supplier-list-create'),
    path('supplier/<int:pk>/', SupplierRetrieveUpdateDeleteAPIView.as_view(), name='supplier-retrieve-update-delete'),
    path('suppliers/<int:pk>/items_supplied/', SupplierItemsSuppliedAPIView.as_view(), name='supplier-items-supplied'),  
]






