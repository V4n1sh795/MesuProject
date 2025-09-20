# Используем официальный образ nginx как базовый
FROM nginx:alpine

# Копируем собственный конфиг nginx (опционально)
# COPY nginx.conf /etc/nginx/nginx.conf

# Копируем статические файлы (HTML, CSS, JS и т.д.) в корневую директорию nginx
COPY ./html /usr/share/nginx/html

# Открываем порт 80 для внешнего доступа
EXPOSE 80

# Запускаем nginx в foreground-режиме (это важно для Docker!)
CMD ["nginx", "-g", "daemon off;"]
