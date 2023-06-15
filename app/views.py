from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app.models import *
from app.serializers import *
from rest_framework.response import Response


class ProductCrudVS(viewsets.ViewSet):
    def list(self,request):
        PQS=Product.objects.all()
        PSD=ProductSerializer(PQS,many=True)
        return Response(PSD.data)

    def create(self,request):
        SD=ProductSerializer(data=request.data)
        if SD.is_valid():
            SD.save()
            return Response({'success':'Product is created'})
        else:
            return Response({'Fail':'Product is not created'})
    
    def retrieve(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO)
        return Response(SPD.data)

    def update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product update'})
        else:
            return Response({'Failed':'Product is not updated'})

    def partial_update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product partialiy update'})
        else:
            return Response({'Failed':'Product is not partially updated'})

    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'Dekete':'Deleted successfully'})



class Pcpc(viewsets.ViewSet):
    def list(self,request):
        PQS=Product_Catagory.objects.all()
        PSD=PCSerializer(PQS,many=True)
        return Response(PSD.data)
        





