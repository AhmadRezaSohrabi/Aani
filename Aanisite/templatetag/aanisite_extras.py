from django.core.urlresolvers import resolve, translate_url

@register.simple_tag(takes_context=True)
def change_language(context, lang=None, *args, **kwargs):
    path = context['request'].path
    return translate_url(path,lang)

