from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import Department,Visit,VisitFor,Visitor
from .serializers import (
UserCreateSerializer,
UserLoginSerializer,
DepartmentSerializer,
VisitForSerializer,
VisitorSerializer,
VisitCreateSerializer,
VisitListSerializer)
from rest_framework.filters import SearchFilter,OrderingFilter
from .paginations import CustomPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            new_data = serializer.data
            return Response(new_data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

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