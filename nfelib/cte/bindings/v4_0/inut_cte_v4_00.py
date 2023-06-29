"""This file was generated by xsdata, v23.6, on 2023-06-28 18:36:32

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.cte.bindings.v4_0.inut_cte_tipos_basico_v4_00 import TinutCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class InutCte(TinutCte):
    """
    Schema XML de validação do Pedido de Inutilização de Numeração do Conhecimento
    de Transportes eletrônico.
    """
    class Meta:
        name = "inutCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
