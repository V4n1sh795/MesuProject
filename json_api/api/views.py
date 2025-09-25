# views.py (без БД)
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.functions import *
@csrf_exempt
def post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        asyncio.run(add_item_to_json(data))
        return JsonResponse("OK")
    if request.method == 'GET':
        return
    return JsonResponse({"error": "POST only"}, status=405)
@csrf_exempt
def get_news(request):
    if request.method == 'GET':
        try:
            data = read_json('news.json')
            print(data)
            return JsonResponse(data, safe=False)  # ← safe=False для списков!
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)