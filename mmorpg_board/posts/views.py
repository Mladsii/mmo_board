from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Response, Category
from .forms import PostForm, ResponseForm



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

def post_list(request):
    """
    Страница со списком всех объявлений.
    """
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    responses = Response.objects.filter(post=post)
    return render(request, 'posts/post_detail.html', {'post': post, 'responses': responses})

@login_required
def add_response(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.post = post
            response.user = request.user
            response.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ResponseForm()
    return render(request, 'posts/post_detail.html', {'form': form, 'post': post})

@login_required
def accept_response(request, pk):
    response = get_object_or_404(Response, pk=pk)
    response.accepted = True
    response.save()
    return redirect('post_detail', pk=response.post.pk)

@login_required
def delete_response(request, pk):
    response = get_object_or_404(Response, pk=pk)
    response.delete()
    return redirect('response_list')

@login_required
def response_list(request):
    """
    Страница с откликами текущего пользователя.
    """
    responses = Response.objects.filter(post__author=request.user)
    return render(request, 'posts/response_list.html', {'responses': responses})