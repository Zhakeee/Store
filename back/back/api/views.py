from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *

class ProductAPIViw(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            u = Products.objects.filter(trash=False)
            return Response( ProductsSerializer(u, many=True).data)

        try:
            instance = Products.objects.get(pk=pk)
        except:
            return Response({})
        # data = ProductsSerializer(instance).data
        return Response(ProductsSerializer(instance).data)
    
    def post(self, request):
        user = ProductsSerializer(data=request.data)
        # print(request.data)
        user.is_valid()
        validated_data = user.validated_data
        user = Products(**validated_data)
        user.save()
        return Response({"message" : "good"})
       

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({})

        try:
            instance = Products.objects.get(pk=pk)
        except:
            return Response({})
        
        serializer = ProductsSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response({})
        else :
            return Response({})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({})

        try:
            instance = Products.objects.get(pk=pk)
        except:
            return Response({})
    
        instance.trash = True
        instance.save()
        return Response({})
    
class TrashAPIViw(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            u = Products.objects.filter(trash=True)
            return Response( ProductsSerializer(u, many=True).data)

        try:
            instance = Products.objects.get(pk=pk)
        except:
            return Response({})
        
        return Response(ProductsSerializer(instance).data)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({})

        try:
            instance = Products.objects.get(pk=pk)
        except:
            return Response({})
        
        
        instance.delete()
        return Response({})

