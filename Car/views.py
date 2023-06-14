from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CarSerializer

# Create your views here.



class selectCarView(APIView):
    def get(self,request,pk=None):
        if pk:  
             try:
                  data= Car.objects.get(pk=pk)
                  serializer = CarSerializer(data,context={"request":request},many = False)
                  return Response(serializer.data)
             except:
                  return Response("could not find an animal!")
    
        data = Car.objects.all()
        serializer = CarSerializer(data,context={"request":request},many=True)
        return Response(serializer.data)


class addCarView(APIView):
    def post(self,request):
        serializer = CarSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class deleteCarView(APIView):
    def delete(self,request,pk):
            event = Car.objects.get(pk=pk)
            event.delete()
            return Response("Deletion successfully!")
         
         






 

 