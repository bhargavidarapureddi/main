from django import template
register=template.Library()

@register.filter
def dollar(value):
    try:
        value = float(value)
        return "${:,.2f}".format(value)
    except (ValueError, TypeError):
        return value
register.filter('doll',dollar)