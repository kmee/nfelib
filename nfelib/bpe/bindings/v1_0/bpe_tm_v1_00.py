"""This file was generated by xsdata, v23.6, on 2023-06-27 01:20:43

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.bpe.bindings.v1_0.bpe_tipos_basico_v1_00 import TbpeTm

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class BpeTm(TbpeTm):
    """
    Bilhete de Passagem Eletrônico Transporte Metropolitano.
    """
    class Meta:
        name = "BPeTM"
        namespace = "http://www.portalfiscal.inf.br/bpe"