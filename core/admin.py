from django.contrib import admin
from .models import Motorista, Veiculo, Rota, RotaVeiculo, Fabrica

# Classe base para configurar propriedades comuns
class ModelAdminBase(admin.ModelAdmin):
    list_per_page = 20

@admin.register(Motorista)
class MotoristaAdmin(ModelAdminBase):
    list_display = (
        'nome',
        'cpf',
        'cnh',
        'data_nascimento',
        'endereco',
        'telefone',
        'email',
    )
    search_fields = (
        'nome',
        'cpf',
    )

@admin.register(Veiculo)
class VeiculoAdmin(ModelAdminBase):
    list_display = (
        'placa',
        'modelo',
        'marca',
        'ano_fabricacao',
    )
    search_fields = (
        'placa',
        'modelo',
    )

@admin.register(Rota)
class RotaAdmin(ModelAdminBase):
    list_display = (
        'data_rota',
        'hora_saida',
        'hora_chegada',
        'motorista',
        'fabrica',
        'quantidade_funcionarios',
        'turno',
    )
    search_fields = (
        'motorista__nome',
        'fabrica__nome_fabrica',
    )

@admin.register(RotaVeiculo)
class RotaVeiculoAdmin(ModelAdminBase):
    list_display = (
        'rota',
        'veiculo',
    )
    search_fields = (
        'rota__id',
        'veiculo__placa',
    )

@admin.register(Fabrica)
class FabricaAdmin(ModelAdminBase):
    list_display = (
        'nome_fabrica',
        'endereco_fabrica',
        'telefone_fabrica',
        'email_fabrica',
    )
    search_fields = (
        'nome_fabrica',
        'endereco_fabrica',
    )
