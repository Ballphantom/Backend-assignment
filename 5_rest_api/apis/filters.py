import django_filters
from .models import Teacher, Student

class TeacherFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(field_name='classrooms__school', distinct=True)
    classroom = django_filters.NumberFilter(field_name='classrooms', distinct=True)
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Teacher
        fields = []

class StudentFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(field_name='classroom__school', distinct=True)
    classroom = django_filters.NumberFilter(field_name='classroom', distinct=True)
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Student
        fields = []
