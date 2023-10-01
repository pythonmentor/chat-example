from django.conf import settings


def agora_app_id(request):
    return {"AGORA_APP_ID": settings.AGORA_APP_ID}
