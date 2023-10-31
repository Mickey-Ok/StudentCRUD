from django.db import models
from django.contrib.auth.models import User

class Students(models.Model):
    fullNames = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    maritalStatus = models.CharField(max_length=10, choices=[('Married', 'Married'), ('Single', 'Single')])
    primaryMaths = models.CharField(max_length=10, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')])
    primaryScience = models.CharField(max_length=10, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')])
    primaryEnglish = models.CharField(max_length=10, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')])
    PrimarymeanGrade = models.CharField(max_length=10, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')])

    highschoolMaths = models.CharField(max_length=10, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')])
    highschoolEnglish = models.CharField(max_length=10, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')])
    highschoolPhysics = models.CharField(max_length=10, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')])
    highschoolChemistry = models.CharField(max_length=10, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')])
    highschoolBiology = models.CharField(max_length=10, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')])
    highschoolGeography = models.CharField(max_length=10, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')])
    SecondarymeanGrade = models.CharField(max_length=10, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')])
    collegeCourseTitle = models.CharField(max_length=100)
    collegeCourseGrade = models.CharField(max_length=100, choices=[
        ('First Class', 'First Class'),
        ('Second Class Upper', 'Second Class Upper'),
        ('Second Class Lower', 'Second Class Lower'),
        ('Pass', 'Pass'),
    ])
    is_admin=models.BooleanField(default=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.fullNames
