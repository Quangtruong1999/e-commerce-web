from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return render(request,'home/index.html')
def index(request):
    return HttpResponseRedirect(reverse('home/index.html'))

def about(request):
    return render(request,'about/about.html')

def blog(request):
    return render(request,'blogs/blog.html')

def contact(request):
    return render(request,'contact/contact.html')

