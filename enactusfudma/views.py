from django.shortcuts import render
from .models import ActiveStudentProfile, AlumniProfile

def home(request):
    return render (request, 'pages/home.html' )

def alumni (request):
    alumniProfile = AlumniProfile.objects.all()
    context = {'alumniProfile': alumniProfile}                                                           
    return render(request, 'pages/alumni.html', context)

def project (request):
    return render(request, 'pages/project.html')

def activeStudent (request):
    activestudent = ActiveStudentProfile.objects.all()
    context = {'activestudent': activestudent}
    return render(request, 'pages/active_student.html', context)
# sgds views
def sdg1 (request):
    return render(request, 'pages/sdgs/sdg1.html')
def sdg2 (request):
    return render(request, 'pages/sdgs/sdg2.html')
def sdg3 (request):
    return render(request, 'pages/sdgs/sdg3.html')
def sdg4 (request):
    return render(request, 'pages/sdgs/sdg4.html')
def sdg5 (request):
    return render(request, 'pages/sdgs/sdg5.html')
def sdg6 (request):
    return render(request, 'pages/sdgs/sdg6.html')
def sdg7 (request):
    return render(request, 'pages/sdgs/sdg7.html')
def sdg8 (request):
    return render(request, 'pages/sdgs/sdg8.html')
def sdg9 (request):
    return render(request, 'pages/sdgs/sdg9.html')
def sdg10 (request):
    return render(request, 'pages/sdgs/sdg10.html')
def sdg11 (request):
    return render(request, 'pages/sdgs/sdg11.html')
def sdg12 (request):
    return render(request, 'pages/sdgs/sdg12.html')
def sdg13 (request):
    return render(request, 'pages/sdgs/sdg13.html')
def sdg14 (request):
    return render(request, 'pages/sdgs/sdg14.html')
def sdg15 (request):
    return render(request, 'pages/sdgs/sdg15.html')
def sdg16 (request):
    return render(request, 'pages/sdgs/sdg16.html')
def sdg17 (request):
    return render(request, 'pages/sdgs/sdg17.html')

    