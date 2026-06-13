# -*- coding: utf-8 -*-

"""
OpenAI Chat Completions API wrapper.
"""

import openai


def converse(
    client: openai.OpenAI,
    model_id: str,
    system: str,
    messages: list[dict],
) -> str:
    """Call OpenAI Chat Completions API and return the assistant's text response."""
    all_messages = [{"role": "system", "content": system}] + messages
    response = client.chat.completions.create(
        model=model_id,
        messages=all_messages,
    )
    return response.choices[0].message.content
