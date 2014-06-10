from django import template
from nomadblog.models import Category

register = template.Library()


@register.assignment_tag
def get_blog_categories():
    return Category.objects.all()
