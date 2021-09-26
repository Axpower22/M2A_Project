from django.core.management.base import BaseCommand
from M2A_app.models import *


def seed_uf():
    UF.objects.bulk_create([
        UF(1, 'AC', 'Acre'),
        UF(2, 'AL', 'Alagoas'),
        UF(3, 'AP', 'Amapá'),
        UF(4, 'AM', 'Amazonas'),
        UF(5, 'BA', 'Bahia'),
        UF(6, 'CE', 'Ceará'),
        UF(7, 'DF', 'Distrito Federal'),
        UF(8, 'ES', 'Espírito Santo'),
        UF(9, 'GO', 'Goiás'),
        UF(10, 'MA', 'Maranhão'),
        UF(11, 'MT', 'Mato Grosso'),
        UF(12, 'MS', 'Mato Grosso do Sul'),
        UF(13, 'MG', 'Minas Gerais'),
        UF(14, 'PA', 'Pará'),
        UF(16, 'PB', 'Paraíba'),
        UF(17, 'PR', 'Paraná'),
        UF(18, 'PE', 'Pernambuco'),
        UF(19, 'PI', 'Piauí'),
        UF(20, 'RJ', 'Rio de Janeiro'),
        UF(21, 'RN', 'Rio Grande do Norte'),
        UF(22, 'RS', 'Rio Grande do Sul'),
        UF(23, 'RO', 'Rondônia'),
        UF(24, 'RR', 'Roraima'),
        UF(25, 'SC', 'Santa Catarina'),
        UF(26, 'SP', 'São Paulo'),
        UF(27, 'SE', 'Sergipe'),
        UF(28, 'TO', 'Tocantins'),
        UF(29, 'EX', 'Estrangeiro'),
    ])


def seed_setor():
    Setor.objects.bulk_create([
        Setor('Agronegócio'),
        Setor('Análise Clínica'),
        Setor('Comércio'),
        Setor('Indústria'),
        Setor('Micro e Pequenas Empresas'),
        Setor('Serviços'),
        Setor('Serviços de Tecnologia da Informação'),
        Setor('Serviços de Turismo'),
        Setor('Serviços Financeiros'),
        Setor('Outro'),
    ])


def seed_segmento():
    Segmento.objects.bulk_create([
        Segmento('Adestramento'),
        Segmento('Agrícultura e Pesca'),
        Segmento('Agroenergia'),
        Segmento('Agronegócio'),
        Segmento('Alimentação'),
        Segmento('Aluguel de Espaço Físico'),
        Segmento('Apicultura'),
        Segmento('Artesanato'),
        Segmento('Biotecnologia'),
        Segmento('Borracharia'),
        Segmento('Café'),
        Segmento('Carne'),
        Segmento('Comércio Varejista'),
        Segmento('Construção Civil'),
        Segmento('Consultoria Comercial'),
        Segmento('Consultoria Empresarial'),
        Segmento('Cosméticos'),
        Segmento('Couro e Calçados'),
        Segmento('Cultura e Entretenimento'),
        Segmento('Derivados de Cana'),
        Segmento('Economia Criativa'),
        Segmento('Estética'),
        Segmento('Fabr. de Prod. de Padaria e Confeitaria'),
        Segmento('Floricultura'),
        Segmento('Fruticultura'),
        Segmento('Horticultura'),
        Segmento('Leite e Derivados'),
        Segmento('Madeira e Móveis'),
        Segmento('Mandiocultura'),
        Segmento('Material de Construção'),
        Segmento('MEI'),
        Segmento('Metal Mecânica'),
        Segmento('Moda'),
        Segmento('Não Informado'),
        Segmento('Ovinocaprinocultura'),
        Segmento('Pet Shop'),
        Segmento('Petróleo e Gás'),
        Segmento('Pizzaria'),
        Segmento('Química e Plásticos'),
        Segmento('Rochas Ornamentais'),
        Segmento('Salão de Beleza'),
        Segmento('Serviços'),
        Segmento('Serviços Financeiros'),
        Segmento('Serviços Médicos'),
        Segmento('Sindicato'),
        Segmento('Tecnologia da Informação'),
        Segmento('Têxtil e Confecções'),
        Segmento('Turismo'),
        Segmento('Outro'),
    ])


def seed_valorArrecadacao():
    ValorArrecadacao.objects.bulk_create([
        ValorArrecadacao('MEI - até R$60 mil'),
        ValorArrecadacao('0 até R$360 mil'),
        ValorArrecadacao('R$360 até R$3.600 mil'),
        ValorArrecadacao('R$3.600 mil até R$5 milhões'),
        ValorArrecadacao('Acima de R$5 milhões'),
    ])


def seed_tipoIndustria():
    TipoIndustria.objects.bulk_create([
        TipoIndustria('Associação/Cooperativa'),
        TipoIndustria('Cliente'),
        TipoIndustria('Filial'),
        TipoIndustria('Fornecedor'),
        TipoIndustria('Franquia'),
        TipoIndustria('Matriz'),
        TipoIndustria('Outros'),
    ])


def seed_situacao():
    Situacao.objects.bulk_create([
        Situacao('Ativo'),
        Situacao('Inativo'),
    ])


def seed_tipoDiagnostico():
    TipoDiagnostico.objects.bulk_create([
        TipoDiagnostico('Simples'),
        TipoDiagnostico('Completo'),
    ])


def seed_faseProjeto():
    FaseProjeto.objects.bulk_create([
        FaseProjeto('T0'),
        FaseProjeto('T1'),
        FaseProjeto('T2'),
        FaseProjeto('T3'),
        FaseProjeto('T4'),
        FaseProjeto('T5'),
    ])


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # seed_tipoDiagnostico()
        # seed_tipoIndustria()
        # seed_situacao()
        # seed_faseProjeto()
        # seed_segmento()
        # seed_setor()
        seed_uf()
        # seed_valorArrecadacao()
