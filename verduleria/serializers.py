from rest_framework import serializers
from .models import Verdura

class VerduraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verdura
        fields = ('id', 'imagen', 'precio', 'nombre')