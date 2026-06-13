# -*- coding: utf-8 -*-

"""Prompt template loading and rendering via Jinja2."""

from pathlib import Path

import jinja2


class PromptTemplate:
    """Thin wrapper around a single Jinja2 template file."""

    def __init__(self, path: Path) -> None:
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(str(path.parent)),
            undefined=jinja2.StrictUndefined,
            keep_trailing_newline=True,
        )
        self._template = env.get_template(path.name)

    def render(self, **kwargs) -> str:
        """Render the template with *kwargs* as context variables."""
        return self._template.render(**kwargs)


class Prompt:
    """A versioned prompt loaded from the ``data/`` directory.

    Parameters
    ----------
    id:
        Absolute path to the prompt's root directory
        (i.e. ``PromptIdEnum.<member>.value``).
    version:
        Version string (e.g. ``"01"``).
    """

    def __init__(self, id: Path, version: str) -> None:
        versions_dir = Path(id) / "versions" / version
        self.system_prompt_template = PromptTemplate(versions_dir / "system-prompt.jinja")
        self.user_prompt_template = PromptTemplate(versions_dir / "user-prompt.jinja")
