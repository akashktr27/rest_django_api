from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from .pagination import CustomPageNumberPagination, CustomLimitOffsetPagination, CustomCursorPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


# Page Number Pagination
class EmployeePageNumberListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPageNumberPagination
    authentication_classes = [JWTAuthentication]

# Limit Offset Pagination
class EmployeeLimitOffsetListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomLimitOffsetPagination

# Cursor Pagination
class EmployeeCursorListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomCursorPagination
