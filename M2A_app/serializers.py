from rest_framework import serializers, generics
from M2A_app import models


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


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Telefone
        fields = ['ddd', 'tipo_telefone', 'telefone']


class FaturamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faturamento
        fields = ['dt_ano', 'valor']


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grupo
        fields = ['nome_grupo']


class EmpresaSerializer(serializers.ModelSerializer):
    fk_segmento = serializers.PrimaryKeyRelatedField(queryset=models.Segmento.objects.all())
    fk_uf = serializers.PrimaryKeyRelatedField(queryset=models.UF.objects.all())
    fk_setor = serializers.PrimaryKeyRelatedField(queryset=models.Setor.objects.all())
    fk_valor_arrecadacao = serializers.PrimaryKeyRelatedField(queryset=models.ValorArrecadacao.objects.all())
    fk_tipo_industria = serializers.PrimaryKeyRelatedField(queryset=models.TipoIndustria.objects.all())
    fk_grupo = serializers.PrimaryKeyRelatedField(queryset=models.Grupo.objects.all(), allow_null=True)

    faturamentos = FaturamentoSerializer(many=True)

    def create(self, validated_data):
        faturamentos = validated_data.pop("faturamentos")
        empresa = models.Empresa.objects.create(**validated_data)

        for faturamento in faturamentos:
            models.Faturamento.objects.create(fk_empresa=empresa, **faturamento)

        return empresa

    class Meta:
        model = models.Empresa
        fields = [
            'cnpj',
            'razao_social',
            'fantasia',
            'bool_master',
            'inscricao_estadual',
            'num_empregados',
            'email',
            'dt_ano_inicio',
            'projeto',
            'nome_gestor',
            'telefone_gestor',
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
            'nome_responsavel',
            'email_responsavel',
            'formacao_responsavel',
            'sexo_responsavel',
            'dt_nascimento_responsavel',
            'cep',
            'logradouro',
            'bairro',
            'cidade',
            'faturamentos'
        ]


class EmpresaVinculadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'


class EmpresaFKSerializer(serializers.Serializer):
    ufs = UFSerializer(many=True)
    setores = SetorSerializer(many=True)
    segmentos = SegmentoSerializer(many=True)
    valores_arrecadacoes = ValorArrecadacaoSerializer(many=True)
    tipos_industria = TipoIndustriaSerializer(many=True)
    grupos = GrupoSerializer(many=True)
    empresas_vinculadas = EmpresaVinculadaSerializer(many=True)


class ListaEmpresaSerializer(serializers.ModelSerializer):
    fk_uf = serializers.SlugRelatedField(queryset=models.UF.objects.all(), slug_field='sg_uf')

    class Meta:
        model = models.Empresa
        fields = ['id', 'fantasia', 'fk_uf', 'fk_master']
