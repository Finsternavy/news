from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.core.exceptions import BadRequest, PermissionDenied
from datetime import datetime
from .models import (
    Section,
    Article,
    ArticleType,
    Status,
)

def redirect_view(request):
    response = redirect('/articles/a/a/')
    return response

class ArticleNavbarHelper:
    def __init__(self, context):
        self.set_section(context)
        self.set_statuses(context)

    def set_section(self, context):
        context["sections"] = Section.objects.all()

    def set_statuses(self, context):
        context["statuses"] = Status.objects.all()

class ArticleListView(ListView):
    template_name = "articles/list.html"
    model = Article

    def get_article_list_context(self, context, section, status):
        context["article_list"] = Article.objects.filter(
            section=section
        ).filter(
            status=status
        ).order_by("created_on").reverse()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status_id = self.kwargs.get("status")
        section_id = self.kwargs.get("section")
        status = Status.objects.get(id=status_id)
        section = Section.objects.get(id=section_id)
        ArticleNavbarHelper(context)

        if status.id == 1:
            return self.get_article_list_context(context, section, status)

        if self.request.user.role.id > 1:
            return self.get_article_list_context(context, section, status)
        raise PermissionDenied("You are not authorized to view this page.")


class ArticleDetailView(DetailView):
    template_name = "articles/detail.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ArticleDraftListView(LoginRequiredMixin, ListView):
    template_name = "articles/draft_list.html"
    model = Article

    def get_article_list_context(self, context, _status):
        context["article_draft_list"] = Article.objects.exclude(status=_status).order_by("created_on").reverse()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = Status.objects.get(id=1)
        print(status)
        ArticleNavbarHelper(context)

        if status.id == 1:
            return self.get_article_list_context(context, status)

        if self.request.user.role.id > 1:
            return self.get_article_list_context(context, status)
        raise PermissionDenied("You are not authorized to view this page.")


class ArticleDraftDetailView(DetailView):
    template_name = "articles/draft_detail.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "articles/new.html"
    model = Article
    fields = ["section", "title", "subtitle", "body", "status"]
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "articles/edit.html"
    model = Article
    fields = ["section", "title", "subtitle", "body", "status"]
    success_url = reverse_lazy('home')

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "articles/delete.html"
    model = Article
    success_url = reverse_lazy('home')

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user



