"""This file was generated by xsdata, v23.6, on 2023-06-27 01:20:36

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.nfe_entrega.bindings.v1_0.leiaute_evento_entrega_nfe_v1_00 import Tevento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class Evento(Tevento):
    """
    Schema XML de validação do evento de comprovante de entrega da NF-e.
    """
    class Meta:
        name = "evento"
        namespace = "http://www.portalfiscal.inf.br/nfe"