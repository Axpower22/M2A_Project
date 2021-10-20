from collections import namedtuple

from rest_framework import viewsets, decorators, views
from rest_framework.response import Response
from M2A_app import models, serializers

EmpresaFKS = namedtuple('EmpresaFKS', ('ufs', 'setores', 'segmentos', 'valores_arrecadacoes', 'tipos_industria', 'grupos'))


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = models.Empresa.objects.all()
    serializer_class = serializers.EmpresaSerializer

    def list(self, request, *args, **kwargs):
        queryset = models.Empresa.objects.all()
        serializer = serializers.ListaEmpresaSerializer(queryset, many=True)
        return Response(serializer.data)


class EmpresaFKSView(views.APIView):
    def get(self, request):
        empresafks = EmpresaFKS(
            ufs=models.UF.objects.all(),
            setores=models.Setor.objects.all(),
            segmentos=models.Segmento.objects.all(),
            valores_arrecadacoes=models.ValorArrecadacao.objects.all(),
            tipos_industria=models.TipoIndustria.objects.all(),
            grupos=models.Grupo.objects.all()
        )
        serialized_empresafks = serializers.EmpresaFKSerializer(empresafks)
        return Response(serialized_empresafks.data)
