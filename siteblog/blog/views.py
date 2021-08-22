from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.



class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context

def index(requests):
    return render(requests, 'blog/index.html')



def get_category(requests, slug):
    return render(requests, 'blog/category.html')


def get_post(requests, slug):
    return render(requests, 'blog/category.html')


class PostByCategory(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2
    allow_empty = False  # Ошибка 404 при запросе несуществующей категории


    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context