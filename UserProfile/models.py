from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Grade(models.Model):
    Term_Choice = [
        ('1', 'Term 1'),
        ('2', 'Term 2'),
    ]

    grade_number = models.IntegerField(null=False, blank=False)
    term = models.CharField(max_length=1, choices=Term_Choice)

    def __str__(self):
        return f"Grade{self.grade_number} - Term{self.get_term_display()}"


class Subjects(models.Model):
    subject_name = models.CharField(max_length=15, blank=False, null=False)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject_name} (Grade {self.grade.grade_number}, {self.grade.get_term_display()})"


class Userprofile(models.Model):
    User_Roles = [
        ('STUDENT' , 'Student'),
        ('TEACHER' , 'Teacher'),
        ('ADMIN' , 'Admin'),

    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=False, blank=False)
    role = models.CharField(max_length=10, choices=User_Roles)
    admission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Video(models.Model):
    title = models.CharField(max_length=50)
    video_file = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
     
    def __str__(self):
        return self.title
    

     
    
     