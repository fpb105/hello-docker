import os

import redis
from django.http import JsonResponse
from django.shortcuts import render

from .models import Message


def index(request):
    return render(request, "hello/index.html")


def api_hello(request):
    message = Message.objects.first()
    r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)
    clicks = r.incr("hello_clicks")
    return JsonResponse({
        "text": message.text if message else None,
        "clicks": clicks,
    })