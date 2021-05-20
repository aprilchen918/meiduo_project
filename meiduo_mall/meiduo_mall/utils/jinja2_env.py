from jinja2 import Environment
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage

def jinja2_environment(**options):
    """jinja2 environment"""

    # Create environment object
    env = Environment(**options)

    # Self-define syntax   {{static('static file related path')}} {{url('namespace of url)}}
    env.globals.update({
        'static': staticfiles_storage.url,    # get prefix of static file
        'url': reverse,   # reverse
    })

    # Return environment object
    return env
