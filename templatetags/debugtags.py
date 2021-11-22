# flake8: noqa
# isort: skip_file
from django import template
from django.conf import settings

from objexplore import explore as _explore
from pudb import set_trace
from rich import inspect as _inspect

register = template.Library()


def require_debug_setting(f):
    """Decorated function is a no-op if TEMPLATE_DEBUG is False"""
    def _(*args, **kwargs):
        TEMPLATE_DEBUG = getattr(settings, 'DEBUG', False)
        return f(*args, **kwargs) if TEMPLATE_DEBUG else ''
    return _


@require_debug_setting
@register.simple_tag(takes_context=True)
def inspect(context, variable=None):
    """
    Presents a richly formatted breakdown of a variable in the cli output.
    """
    try:
        from rich import inspect as _inspect
    except ImportError:
        print("To use the 'inspect' tag, pip install rich.")
        return ""

    if variable:
        _inspect(variable)
    else:
        _inspect(list(context))


@require_debug_setting
@register.simple_tag(takes_context=True)
def explore(context, variable=None):
    """
    Uses objexplore to interactively explore context/var in cli.

    Important: To use this you will need to disable autoreload/threading for django dev server.
    ./manage.py runserver 0.0.0.0:8000 --noreload --nothreading

    This does mean you will need to restart the server manually to see changes.

    Usage: 
    {% explore%}
    """

    try:
        from objexplore import explore as _explore
    except ImportError:
        print("To use the 'explore' tag, pip install objexplore.")
        print("you will also need to disable autoreload/threading for django dev server:")
        print("./manage.py runserver 0.0.0.0:8000 --noreload --nothreading")
        return ""

    if variable:
        _explore(variable)
    else:
        _explore(list(context))


@require_debug_setting
@register.simple_tag(takes_context=True)
def debugger(context, variable=None):
    """
    Enter a debugger in the cli.

    From the debugger you can experiment with the context variables etc.

    Usage:
    {% debugger %}
    """
    try:
        from pudb import set_trace
    except ImportError:
        print("To use the 'debugger' tag, pip install pudb.")
        return ""
    from pprint import pprint as pp
    # Tip: Ctrl+X to enter/exit shell, from there you can interrogate `context` dict.
    # Tip: pretty print is available as pp()
    set_trace()
