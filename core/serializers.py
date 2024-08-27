from rest_framework import serializers
from .models import Motorista, Fabrica, Rota, Veiculo, RotaVeiculo

# Serializer para o modelo Motorista
class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = '__all__'

# Serializer para o modelo Fabrica
class FabricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabrica
        fields = '__all__'

# Serializer para o modelo Rota
class RotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rota
        fields = '__all__'

# Serializer para o modelo Veiculo
class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'

# Serializer para o modelo RotaVeiculo
class RotaVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RotaVeiculo
        fields = '__all__'
