#from django.shortcuts import render
from .models import MenuItem,Category
from .serializers import MenuItemSerializer, CategorySerializer
from rest_framework import generics

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordening_fields = ['price','inventory']
    filter_fields = ['price','inventory']
    search_fields = ['title']

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

