from django import forms
from .models import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

    fullNames = forms.CharField(
        label='Full Names',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    age = forms.IntegerField(
        label='Age',
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )

    gender = forms.ChoiceField(
        label='Gender',
        choices=[('Male', 'Male'), ('Female', 'Female')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    maritalStatus = forms.ChoiceField(
        label='Marital Status',
        choices=[('Married', 'Married'), ('Single', 'Single')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    primaryMaths = forms.ChoiceField(
        label='Primary Maths Grade',
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    primaryScience = forms.ChoiceField(
        label='Primary Science Grade',
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    primaryEnglish = forms.ChoiceField(
        label='Primary English Grade',
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    PrimarymeanGrade = forms.ChoiceField(
        label='Primary Mean Grade',
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-select text-danger'}),
    )

    highschoolMaths = forms.ChoiceField(
        label='High School Maths Grade',
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )



    highschoolScience = forms.ChoiceField(
        label='High School Science Grade',
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    highschoolEnglish = forms.ChoiceField(
        label='High School English Grade',
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    highschoolPhysics = forms.ChoiceField(
        label='High School Physics Grade',
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    highschoolChemistry = forms.ChoiceField(
        label='High School Chemistry Grade',
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    highschoolBiology = forms.ChoiceField(
        label='High School Biology Grade',
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    highschoolGeography = forms.ChoiceField(
        label='High School Geography Grade',
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('notDone', 'Not Done')],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )


    SecondarymeanGrade = forms.ChoiceField(
        label='Secondary Mean Grade',
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-select text-danger'}),
    )

    collegeCourseTitle = forms.CharField(
        label='Title of the Course',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    collegeCourseGrade = forms.ChoiceField(
        label='Course Grade',
        choices=[
            ('First Class', 'First Class'),
            ('Second Class Upper', 'Second Class Upper'),
            ('Second Class Lower', 'Second Class Lower'),
            ('Pass', 'Pass'),
        ],
        widget=forms.Select(attrs={'class': 'form-select text-danger'}),
    )

