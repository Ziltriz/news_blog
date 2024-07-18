from django.views.generic import ListView, DetailView
from .models import Post
class NewsList(ListView):
    queryset = Post.objects.order_by('-date_birth')
    template_name = 'news.html'
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'