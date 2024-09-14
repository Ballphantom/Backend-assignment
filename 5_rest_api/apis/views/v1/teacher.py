from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import Teacher
from apis.serializers import ClassroomSerializer, TeacherSerializer
from rest_framework.permissions import IsAuthenticated

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'gender', 'classrooms__school', 'classrooms']
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.get_serializer(instance).data
        data['classrooms'] = ClassroomSerializer(instance.classrooms.all(), many=True).data
        return Response(data)
