from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def all_blogs(request):
    post_objects = Post.objects.order_by('date')[:5]
    return render(request, 'blog/all_blogs.html', {'posts':post_objects})

def detail(request, blog_id):
    blog = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})