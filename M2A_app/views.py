from collections import namedtuple

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, decorators, views, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from M2A_app import models, serializers
from django.contrib.auth.models import User

EmpresaFKS = namedtuple('EmpresaFKS',
                        ('ufs', 'setores', 'segmentos', 'valores_arrecadacoes', 'tipos_industria', 'grupos',
                         'empresas_vinculadas', 'projetos'))

UsuarioFKS = namedtuple('UsuarioFKS', ('ufs', 'perfis', 'situacoes'))


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = models.Empresa.objects.all()
    serializer_class = serializers.EmpresaSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filterset_fields = ['fk_master', 'fk_uf', 'fk_valor_arrecadacao', 'fk_setor']
    search_fields = ['fantasia']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ListaEmpresaSerializer
        else:
            return serializers.EmpresaSerializer

    @action(detail=True, methods=['GET'])
    def get_questionario(self, request, *args, **kwargs):
        empresa = self.get_object()
        questionario = serializers.QuestionarioSerializer(empresa.questionario)

        return Response(questionario.data)

    @action(detail=False, methods=['POST'])
    def inserir_em_grupo(self, request, *args, **kwargs):
        empresas = request.data["empresas"]
        grupo_id = request.data["grupo_id"]

        grupo = models.Grupo.objects.get(id=grupo_id)

        for empresa_id in empresas:
            empresa = models.Empresa.objects.get(id=empresa_id)
            empresa.fk_grupo = grupo
            empresa.save()

        return Response({"status": 200})

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
            projetos=models.Projeto.objects.all()
        )
        serialized_empresafks = serializers.EmpresaFKSerializer(empresafks)
        return Response(serialized_empresafks.data)


class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = models.Diagnostico.objects.all()
    serializer_class = serializers.DiagnosticoSerializer


class GruposView(views.APIView):
    def post(self, request):
        pass

    def get(self, request):
        serialized = serializers.GrupoSerializer(models.Grupo.objects.all())
        return Response(serialized.data)


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = models.UsuarioInfo.objects.all()
    serializer_class = serializers.UsuarioSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['PUT'])
    def change_password(self, request, *args, **kwargs):
        password = request.data.pop('password')
        confirm_password = request.data.pop('confirmPassword')

        if password != confirm_password:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"password": "Os valores devem ser iguais",
                                                                      "confirmPassword": "Os valores devem ser iguais"})

        user = request.user
        print(user)
        user.set_password(password)

        user.save()

        return Response()

    @action(detail=False, methods=['GET'])
    def consultores(self, request, *args, **kwargs):
        consultores = serializers.UsuarioSerializer(
            models.UsuarioInfo.objects.filter(perfil__nm_perfil__iexact="consultor"), many=True)
        return Response(consultores.data)

    @action(detail=False, methods=['GET'])
    def get_fks(self, request):
        fks = UsuarioFKS(
            ufs=models.UF.objects.all(),
            perfis=models.Perfil.objects.all(),
            situacoes=models.Situacao.objects.all()
        )
        serializer = serializers.UsuarioFKSerializer(fks)

        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def get_usuario(self, request, *args, **kwargs):
        user = request.user
        user = serializers.UsuarioSerializer(user.info)

        return Response(user.data)


class QuestionarioViewset(viewsets.ModelViewSet):
    queryset = models.Questionario.objects.all()
    serializer_class = serializers.QuestionarioSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['POST'])
    def responder(self, request, *args, **kwargs):
        data = request.data
        questionario = self.get_object()

        diagnostico_count = models.Diagnostico.objects.filter(empresa_id=data["empresa"]).count()

        fase = f"T{diagnostico_count}"

        diagnostico = models.Diagnostico.objects.create(
            empresa_id=data["empresa"],
            fase=fase,
            questionario_id=questionario.id,
        )

        for resposta in data["respostas"]:
            models.RespostaQuestionario.objects.create(
                diagnostico=diagnostico,
                pergunta_id=resposta["pergunta"],
                resposta_id=resposta["resposta"],
            )

        return Response(status=status.HTTP_200_OK)
