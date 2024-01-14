from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost

# Post List View
def all_posts_view(request):
    context = dict(
        posts = BlogPost.objects.filter(is_active=True)
    )
    return render(request, 'blog/all_posts.html', context)

# Post Deatil View
def post_detail_view(request, post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug, is_active=True)
    context = dict(
        post=post
    )
    return render(request, 'blog/components/post_detail.html',context)
