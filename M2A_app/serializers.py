from rest_framework import serializers, generics
from M2A_app import models
from django.contrib.auth.models import User
from drf_writable_nested.serializers import WritableNestedModelSerializer


class SegmentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Segmento
        fields = '__all__'


class UFSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UF
        fields = '__all__'


class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Setor
        fields = '__all__'


class ValorArrecadacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ValorArrecadacao
        fields = '__all__'


class TipoIndustriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoIndustria
        fields = '__all__'


class FaturamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faturamento
        fields = ['dt_ano', 'valor']


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grupo
        fields = ['id', 'nome_grupo']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'date_joined', 'is_superuser']


class UsuarioSerializer(WritableNestedModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = models.UsuarioInfo
        fields = ('id', 'user', 'nome', 'telefone', 'situacao', 'perfil', 'uf')

    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data.pop('email')

        user = User.objects.create_user(
            username=email,
            password=password,
        )

        usuario = models.UsuarioInfo.objects.create(user=user.id, email=email, **validated_data)

        return usuario


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsuarioInfo
        fields = '__all__'


class ResponsavelSerializer(serializers.ModelSerializer):
    info = InfoSerializer()

    class Meta:
        model = User
        exclude = ['password', 'last_login', 'date_joined', 'is_superuser']


class EmpresaSerializer(serializers.ModelSerializer):
    fk_segmento = serializers.PrimaryKeyRelatedField(queryset=models.Segmento.objects.all())
    fk_uf = serializers.PrimaryKeyRelatedField(queryset=models.UF.objects.all())
    fk_setor = serializers.PrimaryKeyRelatedField(queryset=models.Setor.objects.all())
    fk_valor_arrecadacao = serializers.PrimaryKeyRelatedField(queryset=models.ValorArrecadacao.objects.all())
    fk_tipo_industria = serializers.PrimaryKeyRelatedField(queryset=models.TipoIndustria.objects.all())
    # fk_grupo = GrupoSerializer(allow_null=True)

    faturamentos = FaturamentoSerializer(many=True)

    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        faturamentos = validated_data.pop("faturamentos")
        usuario = validated_data.pop("usuario")
        empresa = models.Empresa.objects.create(usuario=usuario, **validated_data)

        for faturamento in faturamentos:
            models.Faturamento.objects.create(fk_empresa=empresa, **faturamento)

        return empresa

    class Meta:
        model = models.Empresa
        fields = [
            'id',
            'cnpj',
            'razao_social',
            'fantasia',
            'bool_master',
            'inscricao_estadual',
            'num_empregados',
            'dt_ano_inicio',
            'projeto',
            'telefone',
            'fax',
            'celular',
            'ds_negocio',
            'missao',
            'visao',
            'valores',
            'fk_grupo',
            'fk_master',
            'fk_segmento',
            'fk_setor',
            'fk_valor_arrecadacao',
            'fk_tipo_industria',
            'fk_uf',
            'cep',
            'logradouro',
            'bairro',
            'cidade',
            'faturamentos',
            'usuario',
        ]


class EmpresaPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'


class EmpresaVinculadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'


class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projeto
        fields = '__all__'


class EmpresaFKSerializer(serializers.Serializer):
    ufs = UFSerializer(many=True)
    setores = SetorSerializer(many=True)
    segmentos = SegmentoSerializer(many=True)
    valores_arrecadacoes = ValorArrecadacaoSerializer(many=True)
    tipos_industria = TipoIndustriaSerializer(many=True)
    grupos = GrupoSerializer(many=True)
    empresas_vinculadas = EmpresaVinculadaSerializer(many=True)
    projetos = ProjetoSerializer(many=True)


class FaseList(serializers.ListField):
    child = serializers.CharField()


class DiagnosticoFKSerializer(EmpresaFKSerializer):
    fases = FaseList()


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perfil
        fields = '__all__'


class SituacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Situacao
        fields = '__all__'


class UsuarioFKSerializer(serializers.Serializer):
    ufs = UFSerializer(many=True)
    perfis = PerfilSerializer(many=True)
    situacoes = SituacaoSerializer(many=True)


class ListaEmpresaSerializer(serializers.ModelSerializer):
    fk_uf = serializers.SlugRelatedField(queryset=models.UF.objects.all(), slug_field='sg_uf')

    class Meta:
        model = models.Empresa
        fields = ['id', 'fantasia', 'fk_uf', 'fk_master', 'fk_grupo']


class RespostaQuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RespostaQuestionario
        fields = '__all__'


class DiagnosticoSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer()
    risco = serializers.SerializerMethodField()
    respostas = RespostaQuestionarioSerializer(many=True)

    def get_risco(self, obj):
        risco = 0
        for resposta_questionario in obj.respostas.all():
            risco += resposta_questionario.resposta.valor
        # print(risco)
        return risco

    class Meta:
        model = models.Diagnostico
        fields = ('id', 'empresa', 'risco', 'fase', 'questionario', 'data', 'respostas')


class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resposta
        fields = '__all__'


class PerguntaSerializer(serializers.ModelSerializer):
    respostas = RespostaSerializer(many=True)

    class Meta:
        model = models.Pergunta
        fields = '__all__'


class QuestionarioSerializer(serializers.ModelSerializer):
    perguntas = PerguntaSerializer(many=True)

    class Meta:
        model = models.Questionario
        fields = '__all__'
