from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import School, Teacher, Student
from apis.serializers import SchoolSerializer
from rest_framework.permissions import IsAuthenticated

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.get_serializer(instance).data
        data['classroom_count'] = instance.classrooms.count()
        data['teacher_count'] = Teacher.objects.filter(classrooms__school=instance).distinct().count()
        data['student_count'] = Student.objects.filter(classroom__school=instance).count()
        return Response(data)
