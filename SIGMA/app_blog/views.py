from django.shortcuts import render

def blog_index(request):
    return render(request, 'app_blog/index.html')
