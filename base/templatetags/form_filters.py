from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    # Adiciona a classe diretamente ao campo de formulário.
    field.field.widget.attrs.update({'class': css_class})
    return field

@register.filter(name='add_placeholder')
def add_placeholder(field, placeholder_text):
    # Adiciona o placeholder diretamente ao campo de formulário.
    field.field.widget.attrs.update({'placeholder': placeholder_text})
    return field
