from django.db import models
from django.conf import settings


class SubReddit(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    published = models.BooleanField(default=True)
    subreddit = models.ForeignKey(SubReddit)
    create_date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=6000)

    def __str__(self):
        return str(self.subreddit) + ' - ' + self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    create_date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=800)

    def __str__(self):
        return str(self.author.username) + ' - ' + str(self.post.title)
