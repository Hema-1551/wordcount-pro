from django.http import HttpResponse 
from django.shortcuts import render


def home(request):
     return render(request,'home.html')

def count(request):
     return render(request,'about.html')
def counts(request):
     fulltext=(request.GET['paragraph']),
     wordlist=fulltext.split(),
     print(type(fulltext)),
     return render(request,'counts.html',{'fulltext':fulltext,})