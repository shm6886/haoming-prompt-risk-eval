# -*- coding: utf-8 -*-

"""Custom exceptions for prompt_risk."""


class JsonExtractionError(Exception):
    """Raised when JSON cannot be extracted from LLM output."""

    def __init__(self, raw_output: str) -> None:
        self.raw_output = raw_output
        preview = raw_output[:200]
        if len(raw_output) > 200:
            preview += "..."
        super().__init__(f"Failed to extract JSON from LLM output: {preview!r}")
