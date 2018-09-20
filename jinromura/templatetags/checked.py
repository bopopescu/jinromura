from django import template

register = template.Library()

@register.filter
def _checked(value,querydict):
    people = querydict.getlist('people')
    if str(value) in people:
        return "checked"
    return ""
