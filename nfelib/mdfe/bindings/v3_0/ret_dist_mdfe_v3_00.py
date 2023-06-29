"""This file was generated by xsdata, v23.6, on 2023-06-28 18:36:36

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.mdfe.bindings.v3_0.leiaute_dist_mdfe_v3_00 import TretDistDfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class RetDistMdfe(TretDistDfe):
    """
    Retorno de pedido de distribuição de MDF-e.
    """
    class Meta:
        name = "retDistMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
