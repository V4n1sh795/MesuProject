# views.py (без БД)
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Просто "отзеркаливаем" с изменениями
        result = {
            "received": data,
            "status": "ok",
            "processed_at": "now"
        }
        return JsonResponse(result)
    if request.method == 'GET':
        return
    return JsonResponse({"error": "POST only"}, status=405)