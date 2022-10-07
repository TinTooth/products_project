from itertools import product
from math import prod
from os import stat
from django.urls import is_valid_path
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import status
from .models import Product
from products import serializers


# Create your views here.
@api_view(['GET','POST'])
def products_list(request):

    if request.method == 'GET':
        query_set = Product.objects.all()
        serializer = ProductSerializer(query_set, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status= status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk = pk)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


 