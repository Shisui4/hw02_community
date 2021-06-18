from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group, User


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)

    page_number = request.GET.get('page')

    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page}
    )


def group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    group_list = group.group_post.all().order_by('-pub_date')
    paginator = Paginator(group_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "group.html", {"group": group, "page": page})


def profile(request, username):
    author = get_object_or_404(User, username=username)
    profile_posts = author.posts.all()
    posts_count = profile_posts.count()
    paginator = Paginator(profile_posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'profile.html', {"author": author,
                                            "posts_count": posts_count,
                                            "page": page})


def post_view(request, username, post_id):
    post = get_object_or_404(Post, author__username=username, id=post_id)
    author = post.author
    posts_count = author.posts.count()
    return render(request, 'post.html', {"post": post,
                                         "author": author,
                                         "post_count": posts_count})
