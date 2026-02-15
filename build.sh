#!/usr/bin/env bash

# نصب وابستگی‌ها
pip install -r requirements.txt

# اعمال مهاجرت‌ها
python manage.py migrate

# ساخت superuser (اختیاری، فقط اگر لازم داری)
# export DJANGO_SUPERUSER_USERNAME=admin
# export DJANGO_SUPERUSER_EMAIL=admin@example.com
# export DJANGO_SUPERUSER_PASSWORD=yourpassword
# python manage.py createsuperuser --noinput

# اطمینان از وجود پوشه static
mkdir -p static

# جمع‌آوری فایل‌های استاتیک
python manage.py collectstatic --noinput
