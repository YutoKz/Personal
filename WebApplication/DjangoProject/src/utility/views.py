from django.shortcuts import render

# Create your views here.

def index(request): # type: ignore
    
    return render(request, 'utility/index.html') # type: ignore
