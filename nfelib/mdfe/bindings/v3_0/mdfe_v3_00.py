"""This file was generated by xsdata, v23.6, on 2023-06-28 18:36:36

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.mdfe.bindings.v3_0.mdfe_tipos_basico_v3_00 import Tmdfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class Mdfe(Tmdfe):
    """
    Manisfesto Eletrônico de Documentos Fiscais.
    """
    class Meta:
        name = "MDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
