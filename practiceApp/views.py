from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response 
from .models import *
from .serializers import *
from rest_framework.decorators import action

# Create your views here.

class BookApiView(APIView):
    serializer_class = BookSerializer
    def get(self,request):
        allBooks=Book.objects.all().values()
        return Response({"Message":"List Of Books","Book List":allBooks})
    
    def post(self,request):
        print("Request data is :",request.data)
        serializer_obj = BookSerializer(data=request.data)
        
        if(serializer_obj.is_valid()):

            Book.objects.create(id=serializer_obj.data.get("id"),
                                title=serializer_obj.data.get("title"),
                                author=serializer_obj.data.get("author"))

        book = Book.objects.all().filter(id=request.data['id']).values()
        return Response({"Message":"New Book Added","Book List":book})




class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True,methods=['get'])
    def employee(self,request,pk=None):

        try:

            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(Company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            return Response({
                "message":'Company might not exists !! Error'
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



