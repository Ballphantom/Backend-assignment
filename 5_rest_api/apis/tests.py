from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from apis.models import School, Classroom, Teacher, Student
from rest_framework.authtoken.models import Token

class SchoolAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.school = School.objects.create(
            name="Test School", abbreviation="TS", address="123 Test Avenue"
        )
        self.classroom = Classroom.objects.create(
            school=self.school, grade_level="5", label="5A"
        )
        self.teacher = Teacher.objects.create(
            first_name="John", last_name="Doe", gender="Male"
        )
        self.teacher.classrooms.add(self.classroom)

        self.student = Student.objects.create(
            first_name="Jane", last_name="Doe", gender="Female", classroom=self.classroom
        )

    def test_create_school(self):
        """Test creating a new school"""
        url = reverse('school-list')
        data = {
            'name': 'New School',
            'abbreviation': 'NS',
            'address': '456 New Avenue',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(School.objects.count(), 2)
        self.assertEqual(School.objects.last().name, 'New School')

    def test_retrieve_school(self):
        """Test retrieving a school detail"""
        url = reverse('school-detail', args=[self.school.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test School')

    def test_list_schools(self):
        """Test listing all schools"""
        url = reverse('school-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_school(self):
        """Test updating a school"""
        url = reverse('school-detail', args=[self.school.id])
        data = {
            'name': 'Updated School',
            'abbreviation': 'US',
            'address': '123 Updated Avenue',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.school.refresh_from_db()
        self.assertEqual(self.school.name, 'Updated School')

    def test_delete_school(self):
        """Test deleting a school"""
        url = reverse('school-detail', args=[self.school.id])
        response = self.client.delete(url)
        print(f"Response status code: {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(School.objects.count(), 0)

class ClassroomAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.school = School.objects.create(
            name="Test School", abbreviation="TS", address="123 Test Avenue"
        )
        self.classroom = Classroom.objects.create(
            school=self.school, grade_level="5", label="5A"
        )

    def test_create_classroom(self):
        """Test creating a classroom"""
        url = reverse('classroom-list')
        data = {
            'school': self.school.id,
            'grade_level': '6',
            'label': '6A'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Classroom.objects.count(), 2)

    def test_list_classrooms(self):
        """Test listing classrooms"""
        url = reverse('classroom-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class TeacherAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.school = School.objects.create(
            name="Test School", abbreviation="TS", address="123 Test Avenue"
        )
        self.classroom = Classroom.objects.create(
            school=self.school, grade_level="5", label="5A"
        )
        self.teacher = Teacher.objects.create(
            first_name="John", last_name="Doe", gender="Male"
        )
        self.teacher.classrooms.add(self.classroom)

    def test_create_teacher(self):
        """Test creating a teacher"""
        url = reverse('teacher-list')
        data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'gender': 'Female',
            'classrooms': [self.classroom.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Teacher.objects.count(), 2)

class StudentAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.school = School.objects.create(
            name="Test School", abbreviation="TS", address="123 Test Avenue"
        )
        self.classroom = Classroom.objects.create(
            school=self.school, grade_level="5", label="5A"
        )
        self.student = Student.objects.create(
            first_name="Jane", last_name="Doe", gender="Female", classroom=self.classroom
        )

    def test_create_student(self):
        """Test creating a student"""
        url = reverse('student-list')
        data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'gender': 'Male',
            'classroom': self.classroom.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)
