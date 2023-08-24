from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.

def upload_to_profile(instance, filename):
    random_str = get_random_string(length=8)
    return 'images/profiles/{filename}-{random}'.format(
        filename=filename, random=random_str)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    profile_img = models.ImageField(null=True, blank=True,
                                     upload_to=upload_to_profile)
    bio = models.CharField(null=True, blank=True, max_length=500)
    slug = models.SlugField(unique=True, default='temp')
    like_count = models.PositiveIntegerField(default=0, blank=True)
    post_count = models.PositiveIntegerField(default=0, blank=True)
    comment_count = models.PositiveIntegerField(default=0, blank=True)


    def save(self, *args, **kwargs):
        if self.slug == 'temp':
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    
class Following(models.Model):
    followed_user = models.ForeignKey(User, related_name="followed",
                                        to_field='username',
                                        on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name="followed_by",
                                        on_delete=models.CASCADE,
                                        to_field='username')
    date_followed = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, unique=True, default='temp')
    
    def __str__(self):
        return self.following_user.username + ' followed ' + self.followed_user.username
    
    class Meta:
            constraints = [
                models.UniqueConstraint(
                    fields=["followed_user", "following_user"],
                      name="unique_following_relation"
                )
            ]

    def save(self, *args, **kwargs):
        if self.slug == 'temp':
            self.slug = slugify(self.following_user.username +
                                 ' followed ' + self.followed_user.username)
        return super().save(*args, **kwargs)
