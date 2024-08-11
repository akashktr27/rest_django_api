from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from .pagination import CustomPageNumberPagination, CustomLimitOffsetPagination, CustomCursorPagination

class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]





# Page Number Pagination
class EmployeePageNumberListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPageNumberPagination

# Limit Offset Pagination
class EmployeeLimitOffsetListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomLimitOffsetPagination

# Cursor Pagination
class EmployeeCursorListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomCursorPagination
