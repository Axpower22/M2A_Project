from django.forms import ModelForm
from M2A_app.models import *


# nova_empresa = Empresa(
#     cnpj=body.cnpj,
#     razao_social=body.razao_social,
#     fantasia=body.fantasia,
#     bool_master=body.bool_master,
#     inscricao_estadual=body.inscricao_estadual,
#     num_empregados=body.num_empregados,
#     email=body.email,
#     dt_ano_inicio=body.dt_ano_inicio,
#     projeto=body.projeto,
#     nome_gestor=body.nome_gestor,
#     # grupo=body.grupo,
#     ds_negocio=body.ds_negocio,
#     bool_missao=body.bool_missao,
#     missao=body.missao,
#     bool_visao=body.bool_visao,
#     visao=body.visao,
#     bool_valores=body.bool_valores,
#     valores=body.valores,
#     fk_master=body.fk_master,
#     fk_segmento=body.fk_segmento,
#     fk_setor=body.fk_setor,
#     fk_valor_arrecadacao=body.fk_valor_arrecadacao,
#     fk_tipo_industria=body.fk_tipo_industria,
#     fk_uf=body.fk_uf,
#     cep=body.cep,
#     logradouro=body.logradouro,
#     endereco=body.endereco,
#     bairro=body.bairro,
#     cidade=body.cidade,
# )

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        exclude = ['id', 'fk_master']


class DiagnosticoForm(ModelForm):
    class Meta:
        model = Diagnostico
        exclude = ['id']