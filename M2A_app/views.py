from collections import namedtuple

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, decorators, views, filters
from rest_framework.response import Response
from M2A_app import models, serializers

EmpresaFKS = namedtuple('EmpresaFKS',
                        ('ufs', 'setores', 'segmentos', 'valores_arrecadacoes', 'tipos_industria', 'grupos',
                         'empresas_vinculadas'))


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = models.Empresa.objects.all()
    serializer_class = serializers.EmpresaSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filterset_fields = ['fk_master', 'fk_uf', 'fk_valor_arrecadacao', 'fk_setor']
    search_fields = ['fantasia']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = serializers.ListaEmpresaSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

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
            grupos=models.Grupo.objects.all(),
            empresas_vinculadas=models.Empresa.objects.filter(bool_master=True),
        )
        serialized_empresafks = serializers.EmpresaFKSerializer(empresafks)
        return Response(serialized_empresafks.data)
