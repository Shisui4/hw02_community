from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("group/<slug:slug>/", views.group_post, name="group"),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/<int:post_id>/', views.post_view, name='post'),
]
