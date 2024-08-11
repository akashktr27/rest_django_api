from django.urls import path
from .views import EmployeeListView
from .views import EmployeePageNumberListView, EmployeeLimitOffsetListView, EmployeeCursorListView

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/page/', EmployeePageNumberListView.as_view(), name='employee-page-number-list'),
    path('employees/limit-offset/', EmployeeLimitOffsetListView.as_view(), name='employee-limit-offset-list'),
    path('employees/cursor/', EmployeeCursorListView.as_view(), name='employee-cursor-list'),

]
