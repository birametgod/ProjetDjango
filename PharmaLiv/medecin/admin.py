from django.contrib import admin
from .models import Medecin

# Register your models here.
class MedecinAdmin(admin.ModelAdmin):
	list_display = ('user', 'hopital', 'specialite', )
	ordering = ('specialite', )

admin.site.register(Medecin, MedecinAdmin)
