from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Author, Category


class PostTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='author',email=None, password=None)
        author = Author.objects.create(user=user, username='Zil', rating=1)
        category = Category.objects.create(name='Zil')
        Post.objects.create(author=author, type='post', categories=category, article='Заголовок', text='ТекстТекстТекстТекстТекстТекст',
                            rating=1)

    def test_field_author(self):
        post = Post.objects.get(id=1)
        field_author = post._meta.get_field('author').verbose_name
        self.assertEqual(field_author, 'author')

    def test_field_category(self):
        post = Post.objects.get(id=1)
        field_category = post._meta.get_field('categories').verbose_name
        self.assertEqual(field_category, 'categories')

    def test_field_article(self):
        post = Post.objects.get(id=1)
        field_article = post._meta.get_field('article').verbose_name
        self.assertEqual(field_article, 'article')

    def test_article_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('article').max_length
        self.assertEqual(max_length, 100)

    def test_field_type(self):
        post = Post.objects.get(id=1)
        field_type = post._meta.get_field('type').verbose_name
        self.assertEqual(field_type, 'type')

    def test_type_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('type').max_length
        self.assertEqual(max_length, 9)

    def test_field_text(self):
        post = Post.objects.get(id=1)
        field_text = post._meta.get_field('text').verbose_name
        self.assertEqual(field_text, 'text')

    def test_text_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('text').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_article_name(self):
        post = Post.objects.get(id=1)
        expected_object_name = '%s' % (post.article)
        self.assertEqual(expected_object_name, str(post))

    def test_preview(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.preview(), 'ТекстТекстТекстТекстТекстТекст...')

    def test_like(self):
        post = Post.objects.get(id=1)
        post.like()
        self.assertEqual(post.rating, 2)

    def test_dislike(self):
        post = Post.objects.get(id=1)
        post.dislike()
        self.assertEqual(post.rating, 0)

