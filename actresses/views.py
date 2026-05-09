from django.http import JsonResponse
from .models import Actress

def actress_list(request):

    actresses = list(
        Actress.objects.values("id","name","profile_path")
    )

    return JsonResponse(actresses, safe=False)


from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import Actress

def actress_list(request):
    actresses = list(Actress.objects.values("id", "name", "profile_path"))
    return JsonResponse(actresses, safe=False)

def check_admin(request):
    User = get_user_model()
    users = list(User.objects.values("username", "is_superuser", "is_staff", "is_active"))
    return JsonResponse({"users": users})

def reset_admin(request):
    User = get_user_model()
    try:
        user, created = User.objects.get_or_create(username='glamadmin')
        user.set_password('Glam@2025!')
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return JsonResponse({"status": "✅ Done", "created": created})
    except Exception as e:
        return JsonResponse({"error": str(e)})