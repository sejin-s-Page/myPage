from gc import get_objects
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import BlogPost

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# @login_required
def post_create(request):
    if request.method == 'POST':
        post_form = BlogPost(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('post-list')
    else:
        post_form = BlogPost()
        return render(request, 'blog/post_create.html', {'form': post_form})
