from django.http import JsonResponse
from .models import Actress

def actress_list(request):

    actresses = list(
        Actress.objects.values("id","name","profile_path")
    )

    return JsonResponse(actresses, safe=False)