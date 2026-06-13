# -*- coding: utf-8 -*-

import typing as T
from functools import cached_property

import openai

if T.TYPE_CHECKING:  # pragma: no cover
    from .one_01_main import One


class OneOpenAIMixin:
    @cached_property
    def openai_client(self: "One") -> openai.OpenAI:
        return openai.OpenAI()
