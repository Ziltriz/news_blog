from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import BaseRegisterForm

from .filters import NewsFilter
from .models import Post
from .forms import NewsForm
class NewsList(ListView):
    queryset = Post.objects.order_by('-date_birth')
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class NewsSearch(ListView):
    model = Post
    ordering = 'date_birth'
    template_name = 'news_search.html'
    context_object_name = 'news_search'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsCreate(CreateView):

    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'

class NewsUpdate(LoginRequiredMixin, UpdateView,):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')

class PostCreate(CreateView, PermissionRequiredMixin):
    permission_required = 'news.add_post'
    form_class = NewsForm
    model = Post
    template_name = 'post_create.html'

class PostUpdate(UpdateView, PermissionRequiredMixin):
    permission_required = 'news.update_post'
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('')


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'
