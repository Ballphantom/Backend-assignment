from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import Classroom
from apis.serializers import ClassroomSerializer, TeacherSerializer, StudentSerializer
from rest_framework.permissions import IsAuthenticated

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['school']
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.get_serializer(instance).data
        data['teachers'] = TeacherSerializer(instance.teachers.all(), many=True).data
        data['students'] = StudentSerializer(instance.students.all(), many=True).data
        return Response(data)
