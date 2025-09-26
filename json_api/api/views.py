# views.py (без БД)
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.functions import *
from .models import UploadedImage
from django.shortcuts import render
from django.conf import settings


def my_page(request):
    return render(request, 'app/index.html')

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
@csrf_exempt
def upload_image(request):
    if 'image' not in request.FILES:
        return JsonResponse({'error': 'No image provided'}, status=400)
    
    image_file = request.FILES['image']
    instance = UploadedImage.objects.create(image=image_file)
    
    return JsonResponse({
        'id': instance.id,
        'url': instance.image.url  # Например: /media/uploads/photo.jpg
    })
@csrf_exempt
def get_images(request):
    if request.method =='GET':
    # Путь к папке с изображениями (например, 'media/uploads/')
        media_root = settings.MEDIA_ROOT
        folder_path = os.path.join(media_root, 'uploads')


        # Проверяем, существует ли папка
        if not os.path.exists(folder_path):
            return JsonResponse({'error': 'Folder does not exist'}, status=404)

        # Расширения изображений
        image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')

        # Собираем все изображения
        images = []
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(image_extensions):
                file_path = os.path.join('uploads', filename)  # относительный путь
                images.append({
                    'filename': filename,
                    'url': f"{settings.MEDIA_URL}{file_path}",  # например: /media/uploads/photo.jpg
                })

        return JsonResponse({'images': images})