from django.contrib import admin
from .models import School, Classroom, Teacher, Student

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'address')
    search_fields = ('name', 'abbreviation')

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('grade_level', 'label', 'school')
    search_fields = ('label', 'grade_level')
    list_filter = ('school',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender')
    search_fields = ('first_name', 'last_name')
    list_filter = ('gender',)
    filter_horizontal = ('classrooms',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'classroom')
    search_fields = ('first_name', 'last_name')
    list_filter = ('gender', 'classroom__school')
