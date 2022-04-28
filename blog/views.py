from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from blog.models import Blog
from django.utils.translation import gettext_lazy as _


class BlogListView(ListView):
    template_name = 'blogs.html'
    model = Blog
    paginate_by = 3
    context_object_name = 'blogs'
    queryset = Blog.objects.exclude(id=Blog.objects.last(
    ).id) if Blog.objects.last() else None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_blog'] = Blog.objects.last()
        context['title'] = _('Blog')
        return context


class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = Blog
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['recommended_blogs'] = Blog.objects.exclude(id=self.object.id)[
            :3]
        return context
