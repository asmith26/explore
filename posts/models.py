from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Topic(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    published = models.BooleanField(default=True)
    topic = models.ForeignKey(Topic)
    create_date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=6000)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.id})

    def __str__(self):
        return str(self.topic) + ' - ' + self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    create_date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=800)

    def __str__(self):
        return str(self.author.username) + ' - ' + str(self.post.title)
