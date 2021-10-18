from rest_framework import serializers
from M2A_app import models


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'
