"""
Production settings

- Set secret key from environment variable
"""

from .base import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
