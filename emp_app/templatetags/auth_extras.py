from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    """
    Checks if a given user belongs to a specific group.
    Usage in template: {% if request.user|has_group:"HR Admin" %}
    """
    if not user.is_authenticated:
        return False
    # Superusers automatically have access to everything
    if user.is_superuser:
        return True
    return user.groups.filter(name=group_name).exists()
