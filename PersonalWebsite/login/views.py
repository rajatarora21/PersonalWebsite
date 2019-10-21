from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
     return render(request, 'index.html')

def details(request):
    name=request.POST['name'];
    dob=request.POST['dateOfBirth']
    occupation=request.POST['Occupation']
    religion=request.POST['Religion'];
    city=request.POST['City']
    gender=request.POST['gender']
    data={
        'name':name,
        'dob':dob,
        'occupation':occupation,
        'religion':religion,
        'city':city,
        'gender':gender,
    }
    return render(request,'details.html',data)
def passwordCheck(request):
    name=request.POST['name']
    password=request.POST['password']
    if name=='Rajat' and password=="1234":
        return render(request,'Valid.html')
    else:
        return render(request,'Invalid.html')


