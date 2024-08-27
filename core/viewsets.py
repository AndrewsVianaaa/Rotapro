from rest_framework import viewsets
from .serializers import MotoristaSerializer, FabricaSerializer, RotaSerializer, VeiculoSerializer, RotaVeiculoSerializer
from .models import Motorista, Fabrica, Rota, Veiculo, RotaVeiculo

class MotoristaViewSet(viewsets.ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer
    ordering_fields = '__all__'
    ordering = '-id'

class FabricaViewSet(viewsets.ModelViewSet):
    queryset = Fabrica.objects.all()
    serializer_class = FabricaSerializer
    ordering_fields = '__all__'
    ordering = '-id'

class RotaViewSet(viewsets.ModelViewSet):
    queryset = Rota.objects.all()
    serializer_class = RotaSerializer
    ordering_fields = '__all__'
    ordering = '-id'

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    ordering_fields = '__all__'
    ordering = '-id'

class RotaVeiculoViewSet(viewsets.ModelViewSet):
    queryset = RotaVeiculo.objects.all()
    serializer_class = RotaVeiculoSerializer
    ordering_fields = '__all__'
    ordering = '-id'
