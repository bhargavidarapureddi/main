from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

# Create your views here.
@api_view(['GET'])
def getProductData(request):
    records=Product.objects.all()
    sdata=ProductSerializer(records,many=True)
    return Response(sdata.data)

@api_view(['POST'])
def addProduct(request):
    sdata=ProductSerializer(data=request.data)
    if sdata.is_valid():
        sdata.save()
        return Response(sdata.data)
    return Response(sdata.errors)

@api_view(['PUT'])
def updateProduct(request):
    obj=Product.objects.get(id=request.data['id'])
    sdata=ProductSerializer(obj,data=request.data)
    if sdata.is_valid():
        sdata.save()
        return Response(sdata.data)
    return Response(sdata.errors)

@api_view(['PATCH'])
def partialUpdateProduct(request):
    obj=Product.objects.get(id=request.data['id'])
    sdata=ProductSerializer(obj,data=request.data,partial=True)
    if sdata.is_valid():
        sdata.save()
        return Response(sdata.data)
    return Response(sdata.errors)

@api_view(['DELETE'])
def removeData(request,id):
    obj=Product.objects.get(id=id)
    obj.delete()
    return Response({"status":"success","msg":"record deleted"})