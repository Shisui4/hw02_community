from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group, User
from django.views.generic.base import TemplateView


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
    group_list = group_post.all().order_by('-pub_date')
    paginator = Paginator(group_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "group.html", {"group": group, "page": page})


def profile(request, username):

    return render(request, 'profile.html', {})


def post_view(request, username, post_id):
    profile = get_object_or_404(User, username=username)
    post = profile.posts.filter(id__exact=post_id)
    return render(request, 'post.html', {"profile": profile, "post": post})
