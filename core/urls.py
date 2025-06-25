from django.urls import path
from .views import public_api, protected_api, telegram_webhook

urlpatterns = [
    path('api/public/', public_api, name='public_api'),
    path('api/protected/', protected_api, name='protected_api'),
    path('webhook/telegram/', telegram_webhook, name='telegram_webhook'),
]
