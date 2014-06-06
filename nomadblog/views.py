from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from nomadblog.models import Blog, Category
from nomadblog import get_post_model


DEFAULT_STATUS = getattr(settings, 'PUBLIC_STATUS', 0)
POST_MODEL = get_post_model()


class NomadBlogMixin(object):

    def dispatch(self, request, *args, **kwargs):
        """Get blog object using url param or setting"""
        url_slug = kwargs.get('blog_slug', None)
        default_slug = getattr(settings, 'DEFAULT_BLOG_SLUG', None)
        if not url_slug and not default_slug:
            raise ImproperlyConfigured(u"You must define either a blog_slug url param or a DEFAULT_BLOG_SLUG setting")
        else:
            slug = url_slug and url_slug or default_slug
        if kwargs.get('country_code'):
            blog = get_object_or_404(Blog, countries__code__iexact=self.kwargs.get('country_code'), slug=slug)
        else:
            blog = get_object_or_404(Blog, slug=slug)
        self.blog = blog
        category_slug = kwargs.get('category_slug')
        self.category = get_object_or_404(Category, slug=category_slug) if category_slug else None
        self.country_code = kwargs.get('country_code')
        return super(NomadBlogMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        """Adds blog to context"""
        context = super(NomadBlogMixin, self).get_context_data(*args, **kwargs)
        context['blog'] = self.blog
        context['category'] = self.category
        context['country_code'] = self.country_code
        return context


class PostList(NomadBlogMixin, ListView):
    model = POST_MODEL
    template_name = 'nomadblog/post_list.html'
    paginate_by = getattr(settings, 'POST_PAGINATE_BY', 25)

    def get_queryset(self):
        qs = super(PostList, self).get_queryset()
        return qs.filter(bloguser__blog=self.blog).order_by('-pub_date')


class PostDetail(NomadBlogMixin, DetailView):
    model = POST_MODEL
    template_name = 'nomadblog/post_detail.html'

    def get_object(self, queryset=None):
        queryset = self.get_queryset().filter(bloguser__blog=self.blog, categories=self.category)
        return super(PostDetail, self).get_object(queryset)


class CategoriesList(NomadBlogMixin, ListView):
    model = Category
    paginate_by = getattr(settings, 'CATEGORY_PAGINATE_BY', 25)


class PostsByCategoryList(NomadBlogMixin, ListView):
    model = POST_MODEL
    template_name = 'nomadblog/post_list_by_category.html'
    paginate_by = getattr(settings, 'POST_PAGINATE_BY', 25)

    def get_queryset(self, *args, **kwargs):
        qs = super(PostsByCategoryList, self).get_queryset()
        self.category = get_object_or_404(Category, slug=self.kwargs.get('category_slug', ''))
        return qs.filter(categories=self.category)

    def get_context_data(self, *args, **kwargs):
        context = super(PostsByCategoryList, self).get_context_data(*args, **kwargs)
        context['category'] = self.category
        return context
