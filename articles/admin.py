from django.contrib import admin
from .models import Section, Article, ArticleType, Status

admin.site.register([Section, ArticleType, Article, Status])