"""This file was generated by xsdata, v23.6, on 2023-06-28 18:36:39

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass, field
from enum import Enum
from nfelib import CommonMixin
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


class EvCancBpeDescEvento(Enum):
    CANCELAMENTO = "Cancelamento"


@dataclass
class EvCancBpe(CommonMixin):
    """
    Schema XML de validação do evento do cancelamento 110111.

    :ivar descEvento: Descrição do Evento - “Cancelamento”
    :ivar nProt: Número do Protocolo de Status do BP-e.
    :ivar xJust: Justificativa do Cancelamento
    """
    class Meta:
        name = "evCancBPe"
        namespace = "http://www.portalfiscal.inf.br/bpe"

    descEvento: Optional[EvCancBpeDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    nProt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    xJust: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
