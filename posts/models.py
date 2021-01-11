from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Имя', max_length=200)
    description = models.TextField('Описание')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField("Text")
    pub_date = models.DateTimeField("date_published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,
                              blank=True, null=True, related_name='posts')

    class Meta:
        ordering = ['-pub_date']
