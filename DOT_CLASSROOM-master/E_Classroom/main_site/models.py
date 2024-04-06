from django.db import models


class Student(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    roll_no = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Teacher(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Class(models.Model):
    teacher_email = models.EmailField(max_length=254)
    subject_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.subject_name} - {self.teacher_email}"


'''


from .models import Teacher

# Create a new teacher instance
new_teacher = Teacher(username='teacher_username', password='teacher_password')

# Save the teacher instance to the database
new_teacher.save()
'''

'''
from .models import Student

# Create a new student instance
new_student = Student(email='student_email@example.com', roll_no='123456')

# Save the student instance to the database
new_student.save()

'''

'''
from .models import Student

# Assuming you want to delete a student with a specific email
try:
    student_to_delete = Student.objects.get(email='student_email@example.com')
    student_to_delete.delete()
    print("Student deleted successfully")
except Student.DoesNotExist:
    print("Student does not exist")
'''
