"""This file was generated by xsdata, v23.6, on 2023-06-28 18:36:24

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.nfe_evento_cce.bindings.v1_0.leiaute_cce_v1_00 import Tevento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class Evento(Tevento):
    """
    Schema XML de validação do evento Carta de Correção.
    """
    class Meta:
        name = "evento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
