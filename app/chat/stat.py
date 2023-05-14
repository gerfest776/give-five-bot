import json
import os
import textwrap

import aiofiles
from chat.types import CuEFaResult, StatType
from core.config import settings


class StatManager:
    FILE_EXTENSION = ".json"

    BASE_STAT_TEMPLATE: dict = {
        StatType.TOTAL.value: 0,
        StatType.LOSE.value: 0,
        StatType.WIN.value: 0,
        StatType.DRAW.value: 0,
    }

    SAVE_STAT_CONFIG: dict[CuEFaResult: str | StatType] = {
        CuEFaResult.WIN: StatType.WIN.value,
        CuEFaResult.LOSE: StatType.LOSE.value,
        CuEFaResult.DRAW: StatType.DRAW.value,
    }

    @classmethod
    def __get_user_filename(cls, user_id):
        return os.path.join(settings.STAT_PATH, str(user_id) + cls.FILE_EXTENSION)

    @classmethod
    async def get_user_file(cls, user_id) -> dict:
        filename: str = cls.__get_user_filename(user_id)
        if not os.path.exists(filename):
            return cls.BASE_STAT_TEMPLATE

        async with aiofiles.open(filename, mode="r") as file:
            return json.loads(await file.read())

    @classmethod
    async def save_user_file(cls, user_id, result: CuEFaResult):
        data = await cls.get_user_file(user_id)

        for key in (cls.SAVE_STAT_CONFIG[result], StatType.TOTAL.value):
            data[key] += 1

        async with aiofiles.open(cls.__get_user_filename(user_id), mode="w") as file:
            await file.write(json.dumps(data))

    @classmethod
    async def repr_stat(cls, user_pk: int):
        data = await cls.get_user_file(user_pk)
        return textwrap.dedent(
            f"""
            Общее количество матчей: {data[StatType.TOTAL.value]}
            Побед: {data[StatType.WIN.value]}
            Поражений: {data[StatType.LOSE.value]}
            Ничья: {data[StatType.DRAW.value]}
            """
        )
