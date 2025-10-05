from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.models import Tag

class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('author', password='pass1234')
        self.other = User.objects.create_user('other', password='pass1234')
        self.post = Post.objects.create(title='T', content='C', author=self.user)

    def test_create_comment_requires_login(self):
        url = reverse('blog:comment_create', kwargs={'post_pk': self.post.pk})
        resp = self.client.post(url, {'content': 'hi'})
        self.assertEqual(resp.status_code, 302)  # redirect to login

    def test_create_comment(self):
        self.client.login(username='other', password='pass1234')
        url = reverse('blog:comment_create', kwargs={'post_pk': self.post.pk})
        resp = self.client.post(url, {'content': 'Nice post!'}, follow=True)
        self.assertContains(resp, 'Nice post!')
        self.assertEqual(self.post.comments.count(), 1)

    def test_edit_delete_permissions(self):
        c = Comment.objects.create(post=self.post, author=self.other, content='Hello')
        # other can edit
        self.client.login(username='other', password='pass1234')
        edit_url = reverse('blog:comment_edit', kwargs={'pk': c.pk})
        resp = self.client.get(edit_url)
        self.assertEqual(resp.status_code, 200)
        # someone else cannot edit
        self.client.login(username='author', password='pass1234')
        resp = self.client.get(edit_url)
        # author is different so should be forbidden (302 -> redirect to login) or 403 depending on mixin
        self.assertNotEqual(resp.status_code, 200)
        
    
class TaggingSearchTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('u', 'u@example.com', 'pwd')
        self.p1 = Post.objects.create(author=self.user, title='Django tips', content='Learn django')
        self.p2 = Post.objects.create(author=self.user, title='Python tricks', content='Some python')
        self.p1.tags.add('django', 'web')
        self.p2.tags.add('python', 'tips')

    def test_posts_by_tag(self):
        res = self.client.get('/tags/django/')
        self.assertContains(res, 'Django tips')
        self.assertNotContains(res, 'Python tricks')

    def test_search_by_keyword(self):
        res = self.client.get('/search/?q=python')
        self.assertContains(res, 'Python tricks')
