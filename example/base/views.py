import json
import random
import time

from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.conf import settings

from .models import RoomMember


@require_GET
def lobby(request):
    return render(request, "base/lobby.html")


@require_GET
def room(request):
    return render(request, "base/room.html")


@require_GET
def get_token(request):
    channel_name = request.GET.get("channel")
    uid = random.randint(1, 230)
    expiration_time_in_seconds = 3600
    current_time_stamp = int(time.time())
    privilege_expired_ts = current_time_stamp + expiration_time_in_seconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(
        settings.AGORA_APP_ID,
        settings.AGORA_APP_CERTIFICATE,
        channel_name,
        uid,
        role,
        privilege_expired_ts,
    )

    return JsonResponse({"token": token, "uid": uid})


@require_POST
@csrf_exempt
def create_member(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data["name"], uid=data["UID"], room_name=data["room_name"]
    )

    return JsonResponse({"name": data["name"]})


@require_GET
def get_member(request):
    uid = request.GET.get("UID")
    room_name = request.GET.get("room_name")

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({"name": member.name})


@require_POST
@csrf_exempt
def delete_member(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data["name"], uid=data["UID"], room_name=data["room_name"]
    )
    member.delete()
    return JsonResponse("Member deleted", safe=False)
