from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import *

urlpatterns = [
    path('', Index, name='index'),
    path('contactos/',contactos,name="contactos")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
