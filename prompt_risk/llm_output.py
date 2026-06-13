# -*- coding: utf-8 -*-

"""Utilities for parsing structured data out of raw LLM text responses."""

import json
import re

from .exc import JsonExtractionError

_FENCE_RE = re.compile(r"```(?:json)?\n(.*?)\n```", re.DOTALL)


def extract_json(text: str) -> dict | list:
    """Parse the first JSON value from *text*, stripping Markdown code fences.

    The function first looks for a fenced block (` ```json ... ``` ` or
    ` ``` ... ``` `).  If one is found, only its contents are parsed.
    Otherwise the entire *text* is tried as-is.

    Raises
    ------
    JsonExtractionError
        When no valid JSON can be extracted.
    """
    match = _FENCE_RE.search(text)
    content = match.group(1).strip() if match else text.strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError as exc:
        raise JsonExtractionError(text) from exc
