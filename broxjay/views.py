from django.shortcuts import render, get_object_or_404
from .models import Blog


def main(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {"blogs": blogs})



def detail(request, pk):
    article = get_object_or_404(Blog, pk=pk)
    return render(request, 'detail.html', {"article": article})

def contact(request):
    return render(reguest, 'detail.html')


