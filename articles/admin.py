from django.contrib import admin
from .models import Section, Article, ArticleType

admin.site.register([Section, ArticleType, Article])