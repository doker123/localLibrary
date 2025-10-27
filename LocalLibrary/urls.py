from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView



urlpatterns = [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),

]

# Подгрузка статических файлов
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
