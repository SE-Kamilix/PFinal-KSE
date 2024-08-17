from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Post, Page
from .forms import BlogPostForm

# Create your views here.

def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'app_blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'app_blog/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'app_blog/post_edit.html', {'form': form})

def post_confirm_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'app_blog/post_confirm_delete.html', {'post': post})

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'app_blog/index.html', {'posts': posts})

@login_required
def post_form(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Asigna el usuario autenticado como autor
            post.save()
            return redirect('post_list')
    else:
        form = BlogPostForm()
    return render(request, 'app_blog/post_form.html', {'form': form})


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'app_blog/page_detail.html', {'page': page})

def about(request):
    return render(request, 'app_blog/about.html')


def contact(request):
    return render(request, 'app_blog/contact.html')