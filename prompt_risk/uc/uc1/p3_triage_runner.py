# -*- coding: utf-8 -*-

"""
UC1-P3 triage runner — assign severity and handling priority from P1 + P2 output.
"""

import typing as T
import json
from pydantic import BaseModel, Field, ValidationError

from ...constants import PromptIdEnum
from ...prompts import Prompt
from ...llm_output import extract_json
from ...openai_utils import converse

import openai

T_HANDLING_PRIORITY = T.Literal["urgent", "high", "standard", "low"]


class P3TriageUserPromptData(BaseModel):
    extraction_json: str
    classification_json: str


class P3TriageOutput(BaseModel):
    """Structured output for the P3 severity & priority triage prompt."""

    # fmt: off
    severity_level: int = Field(ge=1, le=5, description="Severity level from 1 (minimal) to 5 (critical)")
    handling_priority: T_HANDLING_PRIORITY = Field(description="Handling priority: urgent, high, standard, or low")
    reasoning: str = Field(description="One or two sentences explaining the triage decision")
    field_conflicts: list[str] = Field(description="Inconsistencies detected between extraction and classification data; empty list if none")
    escalate: bool = Field(description="True if conflicts detected or data too contradictory to triage reliably")
    # fmt: on


MAX_RETRIES = 3
"""Maximum number of API calls per :func:`run_p3_triage` invocation."""


def run_p3_triage(
    client: openai.OpenAI,
    data: P3TriageUserPromptData,
    prompt_version: str = "01",
    model_id: str = "gpt-4o-mini",
) -> P3TriageOutput:
    """Execute the P3 triage prompt and return validated output.

    Takes the structured JSON output from P1 extraction and P2
    classification, and assigns severity level and handling priority.

    Uses the same retry-on-validation-failure pattern as the P1 and P2 runners.
    """
    prompt = Prompt(id=PromptIdEnum.UC1_P3_TRIAGE.value, version=prompt_version)

    system = prompt.system_prompt_template.render()
    user_prompt = prompt.user_prompt_template.render(data=data)
    messages: list[dict] = [
        {"role": "user", "content": user_prompt},
    ]

    for attempt in range(MAX_RETRIES):
        text = converse(client, model_id, system, messages)
        json_obj = extract_json(text)

        try:
            return P3TriageOutput(**json_obj)
        except (json.JSONDecodeError, ValidationError) as exc:
            if attempt == MAX_RETRIES - 1:
                raise

            error_msg = (
                f"Your previous response failed validation:\n{exc}\n\n"
                "Please return a corrected JSON object."
            )
            messages.append({"role": "assistant", "content": text})
            messages.append({"role": "user", "content": error_msg})

    raise Exception("Should never reach this line of code")  # pragma: no cover
