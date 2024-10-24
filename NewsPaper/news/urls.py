from bisect import insort
from xml.sax import parse

from pygments.lexer import include


from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, subscribe, NewsUpdate, NewsDelete, PostDelete, \
    PostUpdate, PostCreate, BaseRegisterView, NewsViewSet, ArticleViewSet
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('<int:pk>', cache_page(60*10)(NewsDetail)),
    path('search/', NewsSearch.as_view(), name='news_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
    path('login/',
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='sign/signup.html'),
         name='signup'),

    path('subscribe/<int:pk>', subscribe, name='subscribe'),
]