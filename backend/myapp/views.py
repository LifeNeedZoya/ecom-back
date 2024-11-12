# myapp/views.py
from django.shortcuts import render
from .models import User

def post_list(request):
    posts = User.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
