from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Paździoch',
        'title': 'Kiepscy',
        'content': 'First post content'
    },
    {
        'author': 'Ferdek',
        'title': 'Kiepscy',
        'content': 'First post content'
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
