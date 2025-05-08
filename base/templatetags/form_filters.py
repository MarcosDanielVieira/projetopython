from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """Adiciona a classe ao campo de formulário."""
    if hasattr(field, 'field') and hasattr(field.field, 'widget'):
        field.field.widget.attrs.update({'class': css_class})
    return field

@register.filter(name='add_placeholder')
def add_placeholder(field, placeholder_text):
    """Adiciona o placeholder ao campo de formulário."""
    if hasattr(field, 'field') and hasattr(field.field, 'widget'):
        field.field.widget.attrs.update({'placeholder': placeholder_text})
    return field
