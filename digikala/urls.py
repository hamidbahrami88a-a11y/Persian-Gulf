# from django.contrib import admin
# from django.urls import path, include
# from . import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('shop.urls')),
#     path('cart/', include('cart.urls')),
#     path('payment/', include('payment.urls'))
# ]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urls.py
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth.models import User
import os

# این فانکشن فقط برای ساخت یک بار سوپر یوزر استفاده میشه
def create_admin(request):
    username = os.environ.get("ADMIN_USERNAME", "admin")
    email = os.environ.get("ADMIN_EMAIL", "admin@example.com")
    password = os.environ.get("ADMIN_PASSWORD", "YourPassword123")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse("Admin created!")
    return HttpResponse("Admin already exists.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('payment/', include('payment.urls')),

    # route موقت برای ساخت سوپر یوزر
    path('create-admin/', create_admin),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

