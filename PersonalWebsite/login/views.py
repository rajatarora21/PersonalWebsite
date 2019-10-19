from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# Create your views here.
def index(request):
    return render(request,'index.html')

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

def chatBot(request):
    bot =ChatBot('ChatBot',storage_adapter='chatterbot.storage.SQLStorageAdapter')
    trainer =ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus.english')
    return render(request,'chatbot.html')
