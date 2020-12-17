from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    
    return render(request, 'posts/index.html',{'posts':Post.objects.all()})

def details(request,received_id):
	post = get_object_or_404(Post, pk=received_id)
	return render(request, 'posts/details.html',{'post':post})