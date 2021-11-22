# Django debug tags

Template tags to help debug django templates.

There are some really useful tools, particularly/recently based on [rich](https://github.com/willmcgugan/rich) that make working with the template variables easier and more enjoyable.

I have currently added these to a templatetags folder you could drop into an existing app in your project, but planned to become a package as part of a wider suite of django/wagtail exploration tools.

`pip install objexplore rich pudb`

In template

```
{% load debugtags %}

..

{% inspect myvar %}
{% explore myvar %}
{% debugger %}

```

Alternatives:

- [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io)
- [django-extensions.debugger_tags](https://django-extensions.readthedocs.io/en/latest/debugger_tags.html)
- [django-debugtools](https://github.com/edoburu/django-debugtools)
- [django-template-debug](https://github.com/calebsmith/django-template-debug) (older)