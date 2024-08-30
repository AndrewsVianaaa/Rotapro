from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Modelo User
class User(AbstractUser, PermissionsMixin):
    name = models.CharField(
        db_column='tx_name',
        max_length=256,
        null=True,
        blank=True,
        verbose_name='Nome Completo'
    )
    email = models.EmailField(
        db_column='tx_email',
        max_length=256,
        null=True,
        blank=True,
        verbose_name='E-mail'
    )
    is_default = models.BooleanField(
        db_column='cs_default',
        default=False,
        verbose_name='Padrão'
    )

    def __str__(self):
        return self.username

    class Meta:
        managed = True
        db_table = 'auth_user'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username']


# Modelo Motorista
class Motorista(models.Model):
    id = models.AutoField(
        db_column='ID_Motorista',  # Corrigido o nome do campo
        primary_key=True,
        verbose_name='ID do Motorista'
    )
    
    nome = models.CharField(
        db_column='Nome',
        max_length=255,
        verbose_name='Nome Completo'
    )
    
    cpf = models.CharField(
        db_column='CPF',
        max_length=50,
        unique=True,
        verbose_name='CPF'
    )
    
    cnh = models.CharField(
        db_column='CNH',
        max_length=50,
        verbose_name='Carteira Nacional de Habilitação'
    )
    
    data_nascimento = models.DateField(
        db_column='Data_Nascimento',
        verbose_name='Data de Nascimento'
    )
    
    endereco = models.CharField(
        db_column='Endereço',
        max_length=255,
        verbose_name='Endereço Completo'
    )
    
    telefone = models.CharField(
        db_column='Telefone',
        max_length=15,
        verbose_name='Número de Telefone'
    )
    
    email = models.EmailField(
        db_column='Email',
        max_length=255,
        verbose_name='Endereço de Email'
    )
    
    class Meta:
        db_table = 'motorista'
        ordering = ['-id']
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'
        
    def __str__(self):
        return self.nome
    

# Modelo Fabrica
class Fabrica(models.Model):
    id = models.AutoField(
        db_column='ID_Fabrica',
        primary_key=True,
        verbose_name='ID da Fábrica'
    )
    
    nome_fabrica = models.CharField(
        db_column='Nome_Fabrica',
        max_length=255,
        verbose_name='Nome da Fábrica'
    )
    
    turno_fabrica = models.CharField(
        db_column='Turno_Fabrica',
        max_length=255,
        verbose_name='Selecione um Turno Comercial'
    )
    
    placa_veiculo = models.CharField(
        db_column='Placa_Veiculo',
        max_length=15,
        verbose_name='Placa do Veículo'
    )
    numero_rota = models.CharField(
        db_column='Numero_Rota',
        max_length=15,
        verbose_name='Número da Rota'
    )
    quantidade_funcionarios = models.CharField(
        db_column='quantidade_funcionarios',
        max_length=15,
        verbose_name='Quantidade de Funcionários'
    )
    data = models.DateField(
        db_column='Data',
        verbose_name='Data'
    )
    hora_inicio = models.CharField(
        db_column='Hora_Inicio',
        max_length=15,
        verbose_name='Hora de Início'
    )

    hora_fim = models.CharField(
        db_column='Hora_Fim',
        max_length=15,
        verbose_name='Data do Término'
    )
    rotas_frequentes = models.CharField(
        db_column='Rotas_Frequentes',
        max_length=1000,
        verbose_name='Rotas Frequentes'
    )

    
    class Meta:
        db_table = 'fabrica'
        ordering = ['nome_fabrica']
        verbose_name = 'Fábrica'
        verbose_name_plural = 'Fábricas'
        
    def __str__(self):
        return self.nome_fabrica


# # Modelo Rota
# class Rota(models.Model):
#     id = models.AutoField(
#         db_column='ID_Rota',
#         primary_key=True,
#         verbose_name='ID da Rota'
#     )
#
#     data_rota = models.DateField(
#         db_column='Data_Rota',
#         verbose_name='Data da Rota'
#     )
#
#     hora_saida = models.TimeField(
#         db_column='Hora_Saida',
#         verbose_name='Horário de Saída'
#     )
#
#     hora_chegada = models.TimeField(
#         db_column='Hora_Chegada',
#         verbose_name='Horário de Chegada'
#     )
#
#     motorista = models.ForeignKey(
#         Motorista,
#         on_delete=models.PROTECT,
#         db_column='ID_Motorista',
#         verbose_name='Motorista'
#     )
#
#     fabrica = models.ForeignKey(
#         Fabrica,
#         on_delete=models.PROTECT,
#         db_column='ID_Fabrica',
#         verbose_name='Fábrica'
#     )
#
#     quantidade_funcionarios = models.IntegerField(
#         db_column='Quantidade_Funcionarios',
#         verbose_name='Quantidade de Funcionários'
#     )
#
#     turno = models.CharField(
#         db_column='Turno',
#         max_length=50,
#         verbose_name='Turno'
#     )
#
#     class Meta:
#         db_table = 'rota'
#         ordering = ['data_rota', 'hora_saida']
#         verbose_name = 'Rota'
#         verbose_name_plural = 'Rotas'
#
#     def __str__(self):
#         return f"Rota {self.id} - {self.motorista.nome} - {self.fabrica.nome_fabrica}"
#
#
# # Modelo Veiculo
# class Veiculo(models.Model):
#     id = models.AutoField(
#         db_column='ID_Veiculo',
#         primary_key=True,
#         verbose_name='ID do Veículo'
#     )
#
#     placa = models.CharField(
#         db_column='Placa',
#         max_length=10,
#         verbose_name='Placa do Veículo'
#     )
#
#     modelo = models.CharField(
#         db_column='Modelo',
#         max_length=100,
#         verbose_name='Modelo do Veículo'
#     )
#
#     marca = models.CharField(
#         db_column='Marca',
#         max_length=100,
#         verbose_name='Marca do Veículo'
#     )
#
#     ano_fabricacao = models.IntegerField(
#         db_column='Ano_Fabricacao',
#         verbose_name='Ano de Fabricação'
#     )
#
#     class Meta:
#         db_table = 'veiculo'
#         ordering = ['marca', 'modelo']
#         verbose_name = 'Veículo'
#         verbose_name_plural = 'Veículos'
#
#     def __str__(self):
#         return f"{self.marca} {self.modelo} - {self.placa}"
#
#
# # Modelo RotaVeiculo
# class RotaVeiculo(models.Model):
#     id = models.AutoField(
#         db_column='ID_Rota_Veiculo',
#         primary_key=True,
#         verbose_name='ID da Relação Rota-Veículo'
#     )
#
#     rota = models.ForeignKey(
#         Rota,
#         on_delete=models.PROTECT,
#         db_column='ID_Rota',
#         verbose_name='Rota'
#     )
#
#     veiculo = models.ForeignKey(
#         Veiculo,
#         on_delete=models.PROTECT,
#         db_column='ID_Veiculo',
#         verbose_name='Veículo'
#     )
#
#     class Meta:
#         db_table = 'rota_veiculo'
#         ordering = ['rota', 'veiculo']
#         verbose_name = 'Rota Veículo'
#         verbose_name_plural = 'Rotas Veículos'
#
#     def __str__(self):
#         return f"Rota {self.rota.id} - Veículo {self.veiculo.placa}"
