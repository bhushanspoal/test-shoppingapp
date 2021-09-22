from django.shortcuts import render

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductsSerializer
from .models import Products

class ProductsList(APIView):

    def get(self, request):
        queryset = Products.objects.all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        pass
