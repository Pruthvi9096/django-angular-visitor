
from django.urls import path,include
from .views import (
    VisitListView,
    VisitCreateView,
    VisitUpdateDeleteView,
    VisitDetailView,
    DepartmentListCreateView,
    DepartmentRetrieveUpdateDeleteView,
    VisitorListCreateView,
    VisitorRetrieveUpdateDeleteView,
    VisitForListCreateView,
    VisitForRetrieveUpdateDeleteView,
    UserRegistrationView,
    UserLoginView
)

urlpatterns = [
    path('login/',UserLoginView.as_view(),name='login'),
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('visits/',VisitListView.as_view(),name='visits'),
    path('visits/create',VisitCreateView.as_view(),name='visit-create'),
    path('visits/r/<int:pk>',VisitDetailView.as_view(),name='visit-detail'),
    path('visits/<int:pk>',VisitUpdateDeleteView.as_view(),name='visit-update-delete'),
    path('departments/',DepartmentListCreateView.as_view(),name='departments'),
    path('departments/<int:pk>',DepartmentRetrieveUpdateDeleteView.as_view(),name='department-detail'),
    path('visitors/',VisitorListCreateView.as_view(),name='visitors'),
    path('visitors/<int:pk>',VisitorRetrieveUpdateDeleteView.as_view(),name='visitor-detail'),
    path('employees/',VisitForListCreateView.as_view(),name='employees'),
    path('employees/<int:pk>',VisitForRetrieveUpdateDeleteView.as_view(),name='employee-detail'),
]
