from django.urls import path
from .views import SchoolViewSet, ClassroomViewSet, TeacherViewSet, StudentViewSet

urlpatterns = [
    path('v1/schools/', SchoolViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='school-list'),
    path('v1/schools/<int:pk>/', SchoolViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='school-detail'),

    # Classrooms
    path('v1/classrooms/', ClassroomViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='classroom-list'),
    path('v1/classrooms/<int:pk>/', ClassroomViewSet.as_view({
        'get': 'retrieve',
        'put': 'update', 
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='classroom-detail'),

    # Teachers
    path('v1/teachers/', TeacherViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='teacher-list'),
    path('v1/teachers/<int:pk>/', TeacherViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='teacher-detail'),

    # Students
    path('v1/students/', StudentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='student-list'),
    path('v1/students/<int:pk>/', StudentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='student-detail'),
]
