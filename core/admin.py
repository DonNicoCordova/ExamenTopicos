from django.contrib import admin
from core.models import Contacto
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'direccion', 'pk', 'thumb' )

    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
            % (obj.imagen.url))
