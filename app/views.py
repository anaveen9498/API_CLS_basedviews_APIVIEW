from django.shortcuts import render


# Create your views here.

from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])
class Productcrud(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        JSO=ProductMS(PQS,many=True)
        return Response(JSO.data)


    def post(self,request):
        PMSD=ProductMS(data=request.data)
        if PMSD.is_valid():
            SPO=PMSD.save()
            return Response({'message':'{} Product is created'.format(SPO)})
        else:
            return Response({'failed':'Product is not created'})

    #def put(self,request,pp):
        #product=Product.objects.get(Pid=pp)
        #PMSD=ProductMS(product,data=request.data)
        #if PMSD.is_valid():
            #SPO=PMSD.save()
            #return Response({'message':'{} Product is Updated'.format(SPO)})
        #else:
            #return Response({'failed':'Product is not Updated'})


    def put(self,request):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=ProductMS(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'Product is Updates'})
        else:
            return Response({'failed':'Product is not Updated'})


