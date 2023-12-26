from rest_framework import serializers
from .models import Company , Employee

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="Enter Book ID")
    title = serializers.CharField(label="Enter Book Title")
    author = serializers.CharField(label="Enter Book Names")
    


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"

