from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Maciek',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': ''
    },
    {
        'author': 'Marian',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': ''
    },
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Fake title'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About' })
