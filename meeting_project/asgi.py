<<<<<<< HEAD
"""
ASGI config for meeting_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meeting_project.settings')

application = get_asgi_application()
=======
 
"""
ASGI config for meeting_project project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meeting_project.settings')
application = get_asgi_application()
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
