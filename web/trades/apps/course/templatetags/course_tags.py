from django import template
from django.db.models import Count


register = template.Library()


@register.simple_tag
def total_courses():
    return 5

