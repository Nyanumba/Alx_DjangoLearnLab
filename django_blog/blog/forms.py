# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post
from .models import Comment
from taggit.forms import TagWidget


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Required. Please enter a valid email address."
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get("email")
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        help_text="Required. Please provide an updated email address."
    )

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "avatar"]

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text='Comma-separated tags', widget=forms.TextInput())
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # published_date and author are auto-set
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': TagWidget(),  # 🔥 enables tag input functionality
        }
        
    def save(self, commit=True):
        # Save instance first, then set tags
        instance = super().save(commit=False)
        if commit:
            instance.save()
        tag_string = self.cleaned_data.get('tags', '')
        # taggit can accept a comma-separated string
        instance.tags.set([t.strip() for t in tag_string.split(',') if t.strip()])
        return instance
        
#comment form
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        max_length=2000,
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']