from django_filters import FilterSet
from .models import Post


class NewsFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            # поиск по названию
            'article': ['icontains'],
            'author__user__username': ['icontains'],
            'date_birth': ['lt'],
        }


