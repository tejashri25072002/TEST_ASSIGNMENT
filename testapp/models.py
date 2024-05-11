from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')

    def __str__(self):
        return self.name

class Lecture(models.Model):
    date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.name} - {self.date}"