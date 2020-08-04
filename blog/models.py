from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=datetime.datetime.now)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return self.title

    # to redirect the create post
    # redirect -- used to redirect to specific route
    # reverse -- will simply return the full url to that route as a string
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
