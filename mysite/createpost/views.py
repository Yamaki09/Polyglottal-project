from django.shortcuts import render
from django.db import models
from blog.models import Post
from createpost.models import CreatePost
from .forms import CreateUserPost

def createPost(request):
    newposts = CreatePost.objects.all()
    oldposts = Post.objects.all()
    form = CreateUserPost()
    if request.method == 'POST':
        form = CreateUserPost(request.POST)
        if form.is_valid():
            p1 = CreatePost(
                user=form.cleaned_data['user'],
                title=form.cleaned_data['title'],
                details=form.cleaned_data['details'],
            )
            p1.save()
    context = {
      "form": form,
      "newposts": newposts,
      "oldposts": oldposts
    }
    return render(request, 'userpage.html', context)