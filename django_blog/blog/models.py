from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#my app models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    
def user_profile_image_path(instance, filename):
    # MEDIA_ROOT/profile_pics/user_<id>/<filename>
    return f'profile_pics/user_{instance.user.id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    # Optional profile picture
    avatar = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True)
    # You can add more fields (location, website, etc.)

    def __str__(self):
        return f"{self.user.username} Profile"

# Auto-create / save profile when user is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()