from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Animal
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AnimalSerializer

# Create your views here.



class selectAnimalView(APIView):
    def get(self,request,pk=None):
        if pk:  
             try:
                  data= Animal.objects.get(pk=pk)
                  serializer = AnimalSerializer(data,context={"request":request},many = False)
                  return Response(serializer.data)
             except:
                  return Response("could not find an animal!")
    
        data = Animal.objects.all()
        serializer = AnimalSerializer(data,context={"request":request},many=True)
        return Response(serializer.data)


class addAnimalView(APIView):
    def post(self,request):
        serializer = AnimalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class deleteAnimalView(APIView):
    def delete(self,request,pk):
            event = Animal.objects.get(pk=pk)
            event.delete()
            return Response("Deletion successfully!")
         
         




















 