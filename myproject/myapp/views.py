from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Properties, Seravice, News

# Create your views here.

def index(request):
    services = Seravice.objects.all()
    news = News.objects.all()

    context = {
        "services": services,
        "news": news,
    }

    return render(request, 'index.html', context)

def about(request):

    return render(request, 'about.html') 

def contact(request):

    return render(request, 'contact.html') 

def property_grid(request):
    properties = Properties.objects.all()

    context = {
        "properties": properties,
        
    }

    return render(request, 'property_grid.html', context) 


def property_single(request, pk):
    propertie = get_object_or_404(Properties, pk=pk)
    if request.method == "POST":                    
        name = request.POST.get('name')      
        email = request.POST.get('email')        
        subject = request.POST.get('subject') 
        message = request.POST.get('message')            
                       
        print(name, email, subject, message)            
        Contactform.objects.create(name=name, email=email, subject=subject, message=message,)       
        return redirect('index') 
    else:


        return render(request, 'property_single.html', {'propertie': propertie})

def founder(request):

    return render(request, 'founder.html')

        


