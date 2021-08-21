from django.shortcuts import render

# Create your views here.


def index(requests):
    return render(requests, 'blog/index.html')



def get_category(requests):
    return render(requests, 'blog/category.html')