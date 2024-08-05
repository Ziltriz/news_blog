from .models import Post, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author',  'type',  'categories',  'article', 'text', 'rating']

class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = []


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )