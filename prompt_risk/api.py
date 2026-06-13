# -*- coding: utf-8 -*-

"""Top-level public API for prompt_risk.

Import this module to access the shared singleton and core helpers without
needing to know the internal package structure::

    from prompt_risk import api
    client = api.one.openai_client
"""

from .one.api import one

__all__ = ["one"]
