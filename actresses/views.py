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
        # Delete all existing users and create fresh
        User.objects.all().delete()
        User.objects.create_superuser(
            username='admin',
            email='admin@glamour.com',
            password='glamour2025'
        )
        return JsonResponse({"status": "✅ Fresh admin created!"})
    except Exception as e:
        return JsonResponse({"error": str(e)})