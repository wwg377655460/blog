#coding:utf8
import datetime
from django.shortcuts import render

# Create your views here.

#现在你的views.py应该是这样
from django.http import HttpResponse

# Create your views here.
from article.models import Article


def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)


