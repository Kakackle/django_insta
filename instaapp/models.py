from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.

class Tag(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(unique=True, max_length=40)
    post_count = models.IntegerField(default=0, blank = True)
    slug = models.SlugField(unique=True, default='temp')

    def save(self, *args, **kwargs):
        if(self.slug=='temp'):
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# sprecyzowanie folderu do ktorego beda uploadowane pliki
def upload_to_post(instance, filename):
    random_str = get_random_string(length=8)
    return 'images/posts/{random}-{filename}'.format(
        filename=filename, random=random_str)

class Post(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name="posts",
                                on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, null=True)
    post_image = models.ImageField(null=True, blank=True,
                                    upload_to=upload_to_post)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    slug = models.SlugField(unique=True, default='temp')
    comment_count = models.PositiveIntegerField(default=0, blank = True)
    view_count = models.PositiveIntegerField(default=0, blank = True)
    like_count = models.PositiveIntegerField(default=0, blank = True)
    liked_by = models.ManyToManyField(User, related_name='liked_posts',
                                    blank=True)

    def save(self, *args, **kwargs):
        if(self.slug=='temp'):
            self.slug = slugify(self.author.profile.slug +
                                '-' + self.description[:25] +
                                '-' + get_random_string(5))
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.slug

class Comment(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name="comments",
                                on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    like_count = models.PositiveIntegerField(default=0, blank = True)
    liked_by = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                              related_name='comments')
    slug = models.SlugField(unique=True, default='temp')

    def save(self, *args, **kwargs):
        if(self.slug=='temp'):
            self.slug = slugify(self.post.slug[:25] +
                                '-' + self.author.profile.slug +
                                '-' + get_random_string(5))
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.slug




# ---------------------------------------------------------------------------- #
#            na przyszlosc, bez sensu jesli masz tylko jeden obrazek           #
# ---------------------------------------------------------------------------- #

class PostImage(models.Model):

    def image_dir(self, filename):
        random_str = get_random_string(length=8)
        return 'images/{post}/{filename}-{random}'.format(
            filename=self.name, post=self.post.slug, random=random_str
        )

    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="post_image_separate")
    image = models.ImageField(upload_to=image_dir)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, default='temp')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == 'temp':
            self.slug = str(self.post.slug) + '-' + str(self.name)
        return super().save(*args, **kwargs)
    



