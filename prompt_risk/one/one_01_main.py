# -*- coding: utf-8 -*-

from .one_02_config import OneConfigMixin
from .one_03_openai import OneOpenAIMixin


class One(
    OneConfigMixin,
    OneOpenAIMixin,
):
    pass

one = One()
