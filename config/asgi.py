"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# 서버 환경에서는 DJANGO_ENVIRONMENT 환경 변수를 'production'으로 설정
os.environ.setdefault('DJANGO_ENVIRONMENT', 'production')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
