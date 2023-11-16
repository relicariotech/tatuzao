from django.contrib import admin

# Register your models here.
from app.models import Cliente, Equipamento, Categoria

class EquipamentoInline(admin.TabularInline):
    model = Equipamento
    extra = 0

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'razao_social', 'telefone', 'cidade')
    inlines = [EquipamentoInline]


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'cliente', 'is_active', 'assembled_on')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')