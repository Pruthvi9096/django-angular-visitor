from django.shortcuts import render
from rest_framework import generics
from .models import Department,Visit,VisitFor,Visitor
from .serializers import (
DepartmentSerializer,
VisitForSerializer,
VisitorSerializer,
VisitCreateSerializer,
VisitListSerializer)
from rest_framework.filters import SearchFilter,OrderingFilter
from .paginations import CustomPagination

class VisitListView(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['visitor_name__name','visit_to__name','purpose']
    pagination_class = CustomPagination

class VisitCreateView(generics.CreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitCreateSerializer

class VisitDetailView(generics.RetrieveAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitListSerializer

class VisitUpdateDeleteView(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitCreateSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['department_name']
    pagination_class = CustomPagination


class DepartmentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class VisitorListCreateView(generics.ListCreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','email','phone','address']
    pagination_class = CustomPagination


class VisitorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

class VisitForListCreateView(generics.ListCreateAPIView):
    queryset = VisitFor.objects.all()
    serializer_class = VisitForSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','department__department_name']
    pagination_class = CustomPagination


class VisitForRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VisitFor.objects.all()
    serializer_class = VisitForSerializer