"""This file was generated by xsdata, v23.6, on 2023-06-28 18:36:22

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.nfe_evento_generico.bindings.v1_0.leiaute_evento_v1_00 import TenvEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class EnvEvento(TenvEvento):
    """
    Schema XML de validação do lote de envio do Evento.
    """
    class Meta:
        name = "envEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
