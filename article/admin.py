from django.contrib import admin

# Register your models here.

from django.contrib import admin
from article.models import Article

# Register your models here.
admin.site.register(Article)