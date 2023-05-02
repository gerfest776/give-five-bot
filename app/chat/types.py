from __future__ import annotations

from enum import Enum, unique
from typing import Any

from chat.custom_exceptions import CuEFaCompareError


@unique
class CuEFaResult(Enum):
    DEFEAT = "DEFEAT"
    WIN = "WIN"
    DRAW = "DRAW"


@unique
class ActionType(Enum):
    GAME = "game"
    STAT = "stat"


@unique
class CuEFaType(Enum):
    SCISSORS = "SCISSORS"
    STONE = "STONE"
    PAPER = "PAPER"

    def __eq__(self, other: CuEFaType | Any) -> CuEFaResult:
        if not isinstance(other, CuEFaType):
            raise CuEFaCompareError
        if self.value == other.value:
            return CuEFaResult.DRAW

        if (
            (self.value == CuEFaType.SCISSORS and other.value == CuEFaType.PAPER)
            or (self.value == CuEFaType.STONE and other.value == CuEFaType.SCISSORS)
            or (self.value == CuEFaType.PAPER and other.value == CuEFaType.STONE)
        ):
            return CuEFaResult.WIN
        return CuEFaResult.DEFEAT
