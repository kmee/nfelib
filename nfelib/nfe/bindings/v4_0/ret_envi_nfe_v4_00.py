"""This file was generated by xsdata, v23.6, on 2023-06-28 18:36:20

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.nfe.bindings.v4_0.leiaute_nfe_v4_00 import TretEnviNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetEnviNfe(TretEnviNfe):
    """
    Schema XML de validação do retorno do Pedido de Concessão de Autorização da
    Nota Fiscal Eletrônica.
    """
    class Meta:
        name = "retEnviNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
