from django.shortcuts import render
from .serializers import FrutasSerializer
from .models import Frutas
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.


class FrutasView(APIView):
    def post(self, request):
        serializer = FrutasSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        frutas = Frutas.objects.all()
        serializer = FrutasSerializer(frutas, many=True)
        return Response(serializer.data)

    
class FrutasCambios(APIView):
    def get_object(self, pk):
        try:
            return Frutas.objects.get(pk=pk)
        except Frutas.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        fruta = self.get_object(pk=pk)
        serializer = FrutasSerializer(fruta, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        fruta = self.get_object(pk=pk)
        fruta.delete()
        return Response(data="Eliminado" ,status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk):
        fruta = self.get_object(pk=pk)
        serializer = FrutasSerializer(fruta)
        return Response(serializer.data)

