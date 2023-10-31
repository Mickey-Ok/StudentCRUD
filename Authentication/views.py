from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import Students
from.forms import StudentsForm



# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def base(request,id=None):
    if request.method == 'POST':
        if id is None:
            # Create a new record
            fullNames = request.POST.get('fullNames')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            maritalStatus = request.POST.get('maritalStatus')
            primaryMaths = request.POST.get('primaryMaths')
            primaryScience = request.POST.get('primaryScience')
            primaryEnglish = request.POST.get('primaryEnglish')
            PrimarymeanGrade = request.POST.get('PrimarymeanGrade')
            highschoolMaths = request.POST.get('highschoolMaths')
            highschoolEnglish = request.POST.get('highschoolEnglish')
            highschoolPhysics = request.POST.get('highschoolPhysics')
            highschoolChemistry = request.POST.get('highschoolChemistry')
            highschoolBiology = request.POST.get('highschoolBiology')
            highschoolGeography = request.POST.get('highschoolGeography')
            SecondarymeanGrade = request.POST.get('SecondarymeanGrade')
            collegeCourseTitle = request.POST.get('collegeCourseTitle')
            collegeCourseGrade = request.POST.get('collegeCourseGrade')

            query = Students(
                fullNames=fullNames,
                age=age,
                gender=gender,
                maritalStatus=maritalStatus,
                primaryMaths=primaryMaths,
                primaryScience=primaryScience,
                primaryEnglish=primaryEnglish,
                PrimarymeanGrade=PrimarymeanGrade,
                highschoolMaths=highschoolMaths,
                highschoolEnglish=highschoolEnglish,
                highschoolPhysics=highschoolPhysics,
                highschoolChemistry=highschoolChemistry,
                highschoolBiology=highschoolBiology,
                highschoolGeography=highschoolGeography,
                SecondarymeanGrade=SecondarymeanGrade,
                collegeCourseTitle=collegeCourseTitle,
                collegeCourseGrade=collegeCourseGrade,
            )
            query.save()
            messages.success(request, 'Form details saved successfully')
        else:
            # Update an existing record
            student = get_object_or_404(Students, pk=id)
            student.fullNames = request.POST.get('fullNames')
            student.age = request.POST.get('age')
            student.gender = request.POST.get('gender')
            student.maritalStatus = request.POST.get('maritalStatus')
            student.primaryMaths = request.POST.get('primaryMaths')
            student.primaryScience = request.POST.get('primaryScience')
            student.primaryEnglish = request.POST.get('primaryEnglish')
            student.PrimarymeanGrade = request.POST.get('PrimarymeanGrade')
            student.highschoolMaths = request.POST.get('highschoolMaths')
            student.highschoolEnglish = request.POST.get('highschoolEnglish')
            student.highschoolPhysics = request.POST.get('highschoolPhysics')
            student.highschoolChemistry = request.POST.get('highschoolChemistry')
            student.highschoolBiology = request.POST.get('highschoolBiology')
            student.highschoolGeography = request.POST.get('highschoolGeography')
            student.SecondarymeanGrade = request.POST.get('SecondarymeanGrade')
            student.collegeCourseTitle = request.POST.get('collegeCourseTitle')
            student.collegeCourseGrade = request.POST.get('collegeCourseGrade')
            student.save()
            messages.success(request, 'Form details updated successfully')


            return redirect('lists')

    form = Students.objects.all()
    context = {
        'students': form,
    }

    return render(request, 'crud/home.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
        else:
            if pass1 != pass2:
                messages.error(request, 'Passwords do not match. Please make sure the passwords match.')
            elif username=='' and pass1=='':
                  messages.error(request, 'Please fill your details')
            else:
                # Create a new user
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')

    return render(request, 'authentication/register.html')

def login_user(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password') 

      user = authenticate(username=username, password=password)

      if user is not None:
            login(request, user)
            return redirect('base', id=user.id)
      else:
            messages.info(request, 'Invalid Credentials. Try Again.')

   return render(request, 'authentication/login.html')

def edit(request, id):
    student = get_object_or_404(Students, pk=id)
    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.info(request, 'Form edited successfully.')
            return redirect('home')  # Redirect back to the home page after editing.
    else:
        form = StudentsForm(instance=student)
    
    context = {'form': form, 'student': student}
    return render(request, 'edit.html', context)

@login_required
def lists(request):
    if request.user.is_authenticated:
        context = {'students': Students.objects.all()}
        return render(request, 'crud/lists.html', context)
    else:
        return render(request, 'unlogged.html')

def form(request):
    return redirect('login')
    # return render (request,'form.html')

def delete(request, id):
    student = Students.objects.get(pk=id)
    student.delete()
    messages.info(request, 'Details deleted succefully.')
    return redirect('lists')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully log out.')
    return redirect('index')










