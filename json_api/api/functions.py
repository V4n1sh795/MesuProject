import json
import asyncio
import os
import uuid

def generate_id():
    return str(uuid.uuid4())

async def add_item_to_json(new_item):
    """
    Добавляет новый словарь в список словарей в JSON-файле.
    
    :param file_path: путь к JSON-файлу (например, 'data.json')
    :param new_item: словарь для добавления, например {'id': 3, 'name': 'Charlie'}
    """
    # Если файл не существует — создаём пустой список
    file_path = "news.json"
    if not os.path.exists(file_path):
        data = []
    else:
        # Читаем существующие данные
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                # Убеждаемся, что это список
                if not isinstance(data, list):
                    raise ValueError("JSON-файл должен содержать список (массив)")
            except json.JSONDecodeError:
                # Если файл повреждён или пуст — начинаем с пустого списка
                data = []

    # Добавляем новый элемент
    new_item['id'] = generate_id()
    data.append(new_item)

    # Записываем обратно в файл
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

async def get_item_by_id(target_id):
    try:
        with open("news.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Предполагается, что data — это список словарей
        for item in data:
            if item.get('id') == target_id:
                return item
        
        return None  # не найдено
    
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

import json

def read_json(file_path):
    """
    Читает JSON-файл и возвращает его содержимое как Python-объект.
    
    :param file_path: путь к файлу (например, 'data.json')
    :return: данные из файла (dict, list и т.д.) или None при ошибке
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка: файл {file_path} содержит некорректный JSON")
        return None