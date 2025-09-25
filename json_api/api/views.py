# views.py (без БД)
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from functions import *

@csrf_exempt
def post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        asyncio.run(add_item_to_json(data))
        return JsonResponse("OK")
    if request.method == 'GET':
        return
    return JsonResponse({"error": "POST only"}, status=405)
@csrf_exempt
def get(request):
    if request.method == 'GET':
        data = asyncio.run(read_json('datacsv/news.json'))
        return JsonResponse(data)