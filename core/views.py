from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TelegramUser
import json


# Public API view
@api_view(['GET'])
@permission_classes([AllowAny])
def public_api(request):
    return Response({"message": "Public Access"})


# Protected API view (authentication required)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_api(request):
    return Response({"message": f"Hello {request.user.username}"})


# Telegram webhook view
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from .models import TelegramUser

@csrf_exempt
def telegram_webhook(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Invalid request method. Use POST.")

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")

    if 'message' in data and data['message'].get('text') == '/start':
        username = data['message']['from'].get('username')
        if username:
            TelegramUser.objects.get_or_create(username=username)

    return JsonResponse({'ok': True})
