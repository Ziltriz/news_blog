from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, related_name='subscribed_categories')

    def __str__(self):
        return f'{self.name}'

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0.0)
    username = models.CharField(max_length=255)

    def update_rating(self):

        articles_rating = Post.objects.filter(author=self).aggregate(Sum('rating'))['rating__sum'] or 0
        comments_rating = Post.objects.filter(author=self).aggregate(Sum('rating'))['rating__sum'] or 0
        article_comments_rating = Post.objects.filter(author=self).aggregate(Sum('comment__rating'))['comment__rating__sum'] or 0

        self.rating = articles_rating + comments_rating + article_comments_rating
        self.save()

    def __str__(self):
        return f'{self.user.username}'


class PostCategories (models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Post (models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    type = models.CharField(choices={'news': 'Новость',
                                     'post': 'Статья'}, max_length=9)
    date_birth = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    article = models.CharField(default='Пустой заголовок', max_length=100)
    text = models.TextField(max_length=1000)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def prewiev(self):
        return self.text[:124] + '...'

    def __str__(self):
        return f'{self.article[:20]}'


class Comment (models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    date_birth = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user





