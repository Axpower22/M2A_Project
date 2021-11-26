from django.db.models import SET_NULL, ForeignKey, DateField, Model

from .empresa import Empresa
from .fase_projeto import FaseProjeto
from .tipo_diagnostico import TipoDiagnostico
from .usuario_info import UsuarioInfo


class Diagnostico(Model):
    dt_ano = DateField()
    tipo = ForeignKey(TipoDiagnostico, on_delete=SET_NULL, null=True)
    fk_empresa = ForeignKey(Empresa, on_delete=SET_NULL, null=True)
    fk_consultor = ForeignKey(UsuarioInfo, on_delete=SET_NULL, null=True)
    fase = ForeignKey(FaseProjeto, on_delete=SET_NULL, null=True)