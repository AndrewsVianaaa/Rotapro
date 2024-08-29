# Generated by Django 5.1 on 2024-08-29 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_veiculo_alter_motorista_id_alter_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rotaveiculo',
            name='rota',
        ),
        migrations.RemoveField(
            model_name='rotaveiculo',
            name='veiculo',
        ),
        migrations.AlterField(
            model_name='fabrica',
            name='data',
            field=models.CharField(db_column='Data', max_length=15, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='fabrica',
            name='hora_inicio',
            field=models.CharField(db_column='Hora_Inicio', max_length=15, verbose_name='Hora de Início'),
        ),
        migrations.AlterField(
            model_name='fabrica',
            name='numero_rota',
            field=models.CharField(db_column='Numero_Rota', max_length=15, verbose_name='Número da Rota'),
        ),
        migrations.AlterField(
            model_name='fabrica',
            name='placa_veiculo',
            field=models.CharField(db_column='Placa_Veiculo', max_length=15, verbose_name='Placa do Veículo'),
        ),
        migrations.AlterField(
            model_name='fabrica',
            name='quantidade_funcionarios',
            field=models.CharField(db_column='quantidade_funcionarios', max_length=15, verbose_name='Quantidade de Funcionários'),
        ),
        migrations.AlterField(
            model_name='fabrica',
            name='rotas_frequentes',
            field=models.CharField(db_column='Rotas_Frequentes', max_length=1000, verbose_name='Rotas Frequentes'),
        ),
        migrations.DeleteModel(
            name='Rota',
        ),
        migrations.DeleteModel(
            name='RotaVeiculo',
        ),
        migrations.DeleteModel(
            name='Veiculo',
        ),
    ]
