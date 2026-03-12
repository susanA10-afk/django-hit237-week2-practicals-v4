from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'blog_app/post_details.html', context)
