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

def reset_admin(request):
    User = get_user_model()
    try:
        if User.objects.filter(username='admin').exists():
            user = User.objects.get(username='admin')
            user.set_password('glamour2025')
            user.is_staff = True
            user.is_superuser = True
            user.save()
            return JsonResponse({"status": "✅ Password reset to glamour2025"})
        else:
            User.objects.create_superuser('admin', 'admin@glamour.com', 'glamour2025')
            return JsonResponse({"status": "✅ Superuser created with password glamour2025"})
    except Exception as e:
        return JsonResponse({"error": str(e)})