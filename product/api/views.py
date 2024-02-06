from rest_framework import views
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from product.models import *
from .serializer import *
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
@api_view(['GET'])
def Hello(request):
    return Response({'msg': 'test'})


@api_view(['GET', 'POST'])
def acceptdata(request):
    print(request.data)
    print(request.method)
    return Response({'msg': 'accept', 'data': request.data})


@api_view(['GET'])
def getAllProducts(request):
    data = Product.product_list()
    datajson = Productserializer(data, many=True).data
    return Response({'msg': 'accept', 'data': datajson})


@api_view(['GET'])
def getProduct(request, proid):
    pro = Product.product_detailes(proid)
    datajson = Productserializer(pro).data
    return Response({'msg': 'accept', 'data':  datajson})


@api_view(['POST'])
def addProduct(request):
    obj = Product()
    # obj.name=request.data['name']
    # obj.image=request.data['image']
    # obj.save()
    obj = Productserializer(data=request.data)
    if (obj.is_valid()):
        obj.save()
        return Response({'msg': 'added'})
    return Response({'msg': 'wrong data', 'error': obj.errors})


@api_view(['PUT'])
def updateProduct(request, proid):
    updateobj = Product.objects.filter(id=proid).first()
    if updateobj:
        serializedProduct = Productserializer(
            instance=updateobj, data=request.data)
        if (serializedProduct.is_valid()):
            return Response(data=serializedProduct.data)
    return Response({'msg': 'product not found', 'error': serializedProduct.errors})



@api_view(['DELETE'])
def deleteProduct(request, proid):
    pro = Product.objects.filter(id=proid).first()
    if pro is not None:  # Check if pro exists
        pro.delete()
        return Response({'msg': 'deleted'})
    return Response({'msg': 'product not found'})


class GetAllProductsg(ListAPIView):
    serializer_class=Productserializer
    queryset=Product.product_list()



class GetAllProductsC(APIView):
    def get(self,request) :
        data = Product.product_list()
        datajson = Productserializer(data, many=True).data
        return Response({'msg': 'accept', 'data': datajson})