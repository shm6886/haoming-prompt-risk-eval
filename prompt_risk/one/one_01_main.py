# -*- coding: utf-8 -*-

from .one_02_config import OneConfigMixin
from .one_03_boto_ses import OneOpenAIMixin


class One(
    OneConfigMixin,
    OneOpenAIMixin,
):
    pass

one = One()
