from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name' : 'Ali', 'age' : '12'},
        {'name' : 'Ahmad', 'age' : '12'}
    ]
    return render(request, "home/index.html", context={'peoples': peoples})

def contact(request):
    return render(request, "home/contact.html")

def about(request):
    return render(request, "home/about.html")
    
def success_page(request):
    return HttpResponse("<h1>Hey this is a success page</h1>")