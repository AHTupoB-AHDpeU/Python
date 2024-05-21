from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-id')[:3]  # filter, get
    title = "Главная страница"
    return render(request, 'my_blog/blog_list.html', {"posts": posts, "title": title})


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    title = post.title
    return render(request, 'my_blog/post_detail.html', {"post": post, "title": title})


def news(request):
    return render(request, 'my_blog/news.html')


def contact(request):
    return render(request, 'my_blog/contact.html')
