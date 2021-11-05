from django.core.management.base import BaseCommand
from M2A_app.models import *


def seed_uf():
    UF.objects.all().delete()
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
    Setor.objects.all().delete()
    Setor.objects.bulk_create([
        Setor(1, 'Agronegócio'),
        Setor(2, 'Análise Clínica'),
        Setor(3, 'Comércio'),
        Setor(4, 'Indústria'),
        Setor(5, 'Micro e Pequenas Empresas'),
        Setor(6, 'Serviços'),
        Setor(7, 'Serviços de Tecnologia da Informação'),
        Setor(8, 'Serviços de Turismo'),
        Setor(9, 'Serviços Financeiros'),
        Setor(10, 'Outro'),
    ])


def seed_segmento():
    Segmento.objects.all().delete()
    Segmento.objects.bulk_create([
        Segmento(1, 'Adestramento'),
        Segmento(2, 'Agrícultura e Pesca'),
        Segmento(3, 'Agroenergia'),
        Segmento(4, 'Agronegócio'),
        Segmento(5, 'Alimentação'),
        Segmento(6, 'Aluguel de Espaço Físico'),
        Segmento(7, 'Apicultura'),
        Segmento(8, 'Artesanato'),
        Segmento(9, 'Biotecnologia'),
        Segmento(10, 'Borracharia'),
        Segmento(11, 'Café'),
        Segmento(12, 'Carne'),
        Segmento(13, 'Comércio Varejista'),
        Segmento(14, 'Construção Civil'),
        Segmento(15, 'Consultoria Comercial'),
        Segmento(16, 'Consultoria Empresarial'),
        Segmento(17, 'Cosméticos'),
        Segmento(18, 'Couro e Calçados'),
        Segmento(19, 'Cultura e Entretenimento'),
        Segmento(20, 'Derivados de Cana'),
        Segmento(21, 'Economia Criativa'),
        Segmento(22, 'Estética'),
        Segmento(23, 'Fabr. de Prod. de Padaria e Confeitaria'),
        Segmento(24, 'Floricultura'),
        Segmento(25, 'Fruticultura'),
        Segmento(26, 'Horticultura'),
        Segmento(27, 'Leite e Derivados'),
        Segmento(28, 'Madeira e Móveis'),
        Segmento(29, 'Mandiocultura'),
        Segmento(30, 'Material de Construção'),
        Segmento(31, 'MEI'),
        Segmento(32, 'Metal Mecânica'),
        Segmento(33, 'Moda'),
        Segmento(34, 'Não Informado'),
        Segmento(35, 'Ovinocaprinocultura'),
        Segmento(36, 'Pet Shop'),
        Segmento(37, 'Petróleo e Gás'),
        Segmento(38, 'Pizzaria'),
        Segmento(39, 'Química e Plásticos'),
        Segmento(40, 'Rochas Ornamentais'),
        Segmento(41, 'Salão de Beleza'),
        Segmento(42, 'Serviços'),
        Segmento(43, 'Serviços Financeiros'),
        Segmento(44, 'Serviços Médicos'),
        Segmento(45, 'Sindicato'),
        Segmento(46, 'Tecnologia da Informação'),
        Segmento(47, 'Têxtil e Confecções'),
        Segmento(48, 'Turismo'),
        Segmento(49, 'Outro'),
    ]), 
1, 

def seed_valorArrecadacao():
    ValorArrecadacao.objects.all().delete()
    ValorArrecadacao.objects.bulk_create([
        ValorArrecadacao(1, 'MEI - até R$81 mil'),
        ValorArrecadacao(2, '0 até R$360 mil'),
        ValorArrecadacao(3, 'R$360 até R$3.600 mil'),
        ValorArrecadacao(4, 'R$3.600 mil até R$5 milhões'),
        ValorArrecadacao(5, 'Acima de R$5 milhões'),
    ])


def seed_tipoIndustria():
    TipoIndustria.objects.all().delete()
    TipoIndustria.objects.bulk_create([
        TipoIndustria(1, 'Associação/Cooperativa'),
        TipoIndustria(2, 'Cliente'),
        TipoIndustria(3, 'Filial'),
        TipoIndustria(4, 'Fornecedor'),
        TipoIndustria(5, 'Franquia'),
        TipoIndustria(6, 'Matriz'),
        TipoIndustria(7, 'Outros'),
    ])


def seed_situacao():
    Situacao.objects.all().delete()
    Situacao.objects.bulk_create([
        Situacao(1, 'Ativo'),
        Situacao(2, 'Inativo'),
    ])


def seed_tipoDiagnostico():
    TipoDiagnostico.objects.all().delete()
    TipoDiagnostico.objects.bulk_create([
        TipoDiagnostico(1, 'Simples'),
        TipoDiagnostico(2, 'Completo'),
    ])


def seed_faseProjeto():
    FaseProjeto.objects.all().delete()
    FaseProjeto.objects.bulk_create([
        FaseProjeto(1, 'T0'),
        FaseProjeto(2, 'T1'),
        FaseProjeto(3, 'T2'),
        FaseProjeto(4, 'T3'),
        FaseProjeto(5, 'T4'),
        FaseProjeto(6, 'T5'),
    ])


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        seed_tipoDiagnostico()
        seed_tipoIndustria()
        seed_situacao()
        seed_faseProjeto()
        seed_segmento()
        seed_setor()
        seed_uf()
        seed_valorArrecadacao()
