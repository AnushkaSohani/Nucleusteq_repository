from django import template

register = template.Library()

@register.filter
def get_ids(queryset):
    return queryset.values_list('id', flat=True)
