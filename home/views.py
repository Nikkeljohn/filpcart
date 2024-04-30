from django.shortcuts import render
from home.models import Contact
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact_us(request):
    context={}
    if request.method == "POST":
        name = request.POST.get("name")
        em = request.POST.get("email")
        sub = request.POST.get("subject")
        msz = request.POST.get("message")
        
        obj = Contact(name = name, email = em, subject = sub, message = msz)
        obj.save()
        context['message']=f"Dear {name}, Thanks for your time!"

    return render(request, 'home/contact.html', context)