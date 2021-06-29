from django.contrib import admin

# Register your models here.
from .models import Contato, Comentario, Quiz, Sala, Aula


class AulaAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'titulo',
                    'sala',
                    'duracao')


class ContatoAdmin(admin.ModelAdmin):
    filter_horizontal = ('aulas', )


admin.site.register(Comentario)
admin.site.register(Quiz)
admin.site.register(Sala)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Contato, ContatoAdmin)
